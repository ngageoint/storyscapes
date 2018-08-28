Working with Services
=====================

Exchange supports the addition of Web Map Service layers and ArcGIS REST Service (ImageServer and MapServer only) layers. This allows a user to add remote web service layers, and combine them with existing layers to create a better, more detailed map.

Add a remote service
--------------------

Exchange users are able to nominate external services, while those with administrator permissions, or those belonging to the csw_manager group, can then “publish” the layer so that it is available to all users.

1. Click the :guilabel:`Data` link on the Exchange toolbar, and select Remote Services in the drop-down menu to open the Remote Services page.

  .. figure:: img/remote-services-menu.png

2. Click the :guilabel:`Register a new Service` button to add a new external layer.

  .. figure:: img/remote-services.png

3. Fill in the service information with the URL. Select either Web Map Service or ArcGIS REST as the Service type from the drop-down menu. When you’re finished, click the :guilabel:`Submit` button.

**Note:** Ensure all extra spaces have been removed from the URL. The service will not register if there are any trailing spaces.

You will be notified that the service was added successfully.

  .. figure:: img/register-new-service.png

All of the layers within the service will be listed. Deselect the checkbox next to any layers that you do not wish to import.

4. Click the :guilabel:`Import Resources` button when you have made your selections. The service will then be available, and can be discovered through Exchange Search and Explore.

  .. figure:: img/available-resources.png

All of the information for the service, including any abstract description, service type and associated keywords, will be listed on the next page. A contact link will be available, so should you have questions, you can reach the individual who added the service to Exchange.

  .. figure:: img/service-resources.png

You can view the details page for a resource by clicking on the title of one of the layers.

Managing services
-----------------

Edit Service Metadata
^^^^^^^^^^^^^^^^^^^^^

Metadata provides the user with more information about the dataset. The more information made available, the better understanding the user will have of the data.

1. From the information page of the service, click the :guilabel:`Edit Service Metadata` button.

  .. figure:: img/manage-services.png

2. Provide as much information as possible. Several of the fields are mandatory, and require your response.

  * **Classification/Caveat** - If your data has a classification, it may be required for that to be populated according to your standard operating procedures.

  * **Title** - It may be helpful to edit the title of the layer, as many of the services import with very generic titles.

  * **Category** - Select a corresponding category to your data.

  * **License** - If your data does not have any associated licenses, select Public Domain from the list.

  * **Provenance** - Indicates the producer of the data content.

  * **Fees** - If there are no fees associated to your data, type “none.”

  .. figure:: img/edit-service.png

3. When you’re finished, click the :guilabel:`Save` button.

Servcie updates
^^^^^^^^^^^^^^^

Select the :guilabel:`Scan Service for Resources` button to check for updated or additional resources to the service.

Any new services will be added to the list.

Remove a service
^^^^^^^^^^^^^^^^

If a service is no longer needed, or the information becomes obsolete, an administrator can easily remove it from Exchange.

1. From the information page of the service, click the :guilabel:`Manage Services` button, and select **Remove Service** from the list.

2. Click the :guilabel:`Yes, I am sure` button to verify your selection.

Access service URLs within Exchange
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

All Exchange layers have service endpoints available to users from the search results list. Users can access the URLs, which can then be used in other programs such as ArcGIS or QGIS.

1. Click the link under the layer description to copy the URL to the clipboard.

2. Paste the URL where required to register the service.

  .. figure:: img/copy-clipboard.png
