'use strict';
//Clarence
(function(){
  angular.module('cart', ['ngCookies'])
    .controller('CartList', function($scope, cart){
      $scope.cart = cart;
      $scope.layers_params = '';

      $scope.newMap = function(){
        var items = cart.getCart().items;
        var params = '';
        for(var i=0; i<items.length; i++){
          // check to see if the item is a registry layer.
          var layer_name = '';
          if(items[i].registry_url) {
            layer_name = 'registry:' + items[i].id;
          } else {
            layer_name = items[i].typename;
          }
          params += 'layer=' + layer_name + '&';
        }
        window.location = '/maps/new?' + params;
      }

      $scope.bulk_perms_submit = function(){
        var items = cart.getCart().items;
        var permissions = permissionsString($('#permission_form'), 'base');
        var selected_ids = $.map(items, function(item){return item.id});
        var message = $('#bulk_perms_message');
        if(selected_ids.length == 0){
         message.find('.message').html('Please select at least one resource to set the permissions');
         message.addClass('alert-danger').removeClass('alert-success alert-warning hidden');
         return;
        }
        $.ajax(
         {
           type: "POST",
           url: "/security/bulk-permissions",
           data: {
             permissions: JSON.stringify(permissions),
             resources: selected_ids
           },
           success: function(data) {
             var not_changed = $.parseJSON(data).not_changed;
             if (not_changed.length > 0){
               message.find('.message').html('Permissions correctly registered, although the following resources were'+
                   ' skipped because you don\'t have the rights to edit their permissions:');
               message.find('.extra_content').html(not_changed.join('</br>'));
               message.addClass('alert-warning').removeClass('alert-success alert-danger hidden');
             }
             else{
               message.find('.message').html('Permissions correctly registered.');
               message.addClass('alert-success').removeClass('alert-warning alert-danger hidden');
             }
           },
           error: function(data){
             message.find('.message').html($.parseJSON(data).error);
             message.addClass('alert-danger').removeClass('alert-success alert-warning hidden');
           }
         }
        );
      };
    })

    .directive('resourceCart', [function(){
      return {
        restrict: 'E',
        templateUrl: "/static/js/search/workspace.html"
      };
    }])

    .service('cart', function($cookies){

      this.init = function(){
        this.$cart = {
          items: this.fillCart()
        };
      };

      this.fillCart = function(){
        // This will fail if angular<1.4.0
        try {
          var geonodeCart = $cookies.getAll();
        } catch(err) {
          var geonodeCart = null;
        }
        var cartSession = [];
        if (geonodeCart !== null) {
          if(Object.keys(geonodeCart).length > 1) {
            Object.keys(geonodeCart).forEach(function(key,index) {
              if(key !== 'csrftoken') {
                try {
                  var obj = JSON.parse(geonodeCart[key]);
                  obj['$$hashKey'] = "object:" + index;
                  cartSession.push(obj);
                } catch(err) {
                  console.log("Cart Session Issue: " + err.message);
                }
              }
            });
          }
        }

        return cartSession;
      };

      this.getCart = function(){
        return this.$cart;
      }

      this.addItem = function(item){

        if(!item.id && item.layer_identifier){
          item.id = item.layer_identifier;
        }

        if(this.getItemById(item.id) === null){
          this.getCart().items.push(item);
          $cookies.putObject(item['uuid'], {uuid: item['uuid'], title: item['title'], typename: item['typename'], id: item['id']}, {path: '/'});
        }
      }

      this.removeItem = function(item){
        if(this.getItemById(item.id) !== null){
          var cart = this.getCart();
          angular.forEach(cart.items, function(cart_item, index){
            if(cart_item.id === item.id){
              cart.items.splice(index, 1);
              $cookies.remove(cart_item['uuid'], {path: '/'});
            }
          });
        }
      }

      this.toggleItem = function(item){
        if(this.getItemById(item.id) === null){
          this.addItem(item);
        }else{
          this.removeItem(item);
        }
      }

      this.getItemById = function (itemId) {
        var items = this.getCart().items;
        var the_item = null;
        angular.forEach(items, function(item){
          if(item.id === itemId){
            the_item = item;
          }
        });
        return the_item;
      }

      this.getFaClass = function(id){
        if(this.getItemById(id) === null){
          return 'fa-plus';
        }else{
          return 'fa-remove';
        }
      }

      this.getThumbnailUrl = function(item) {
        var parts = item.detail_url.split('/').slice(-2);
        return '/thumbnails/' + parts[0] + '/' + parts[1];
      }
    })

    .run(['cart', function(cart){
      cart.init();
    }])
})();
