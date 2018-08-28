Discovering Exchange Content
=============================

There are many different ways to find, filter and display data throughout Exchange. Whether you know what you’re looking for, or you need to do a little digging, Exchange helps you find exactly what you need.

Exchange Search
^^^^^^^^^^^^^^^

Using just one search, you can find all of the maps, layers or documents that have been uploaded into Exchange, as well as external layers added by other users. This makes finding data in Exchange fast and easy.

From the Boundless Exchange homepage, simply enter your search term in the Search for Content field, and press Enter. Select a resource from the list, and click the View Details link to open its information page, or use additional filters to refine your search even more. Click the title of the resource to add it directly to a map.

You can use multiple words to do a simple search. This type of search does not require the use of wildcards or Boolean operators. If you search for “te”, you will get a list of all of the results that have words beginning with the letter combination “te” somewhere in each result’s information.

Additional Ways to Search
-------------------------
The Exchange Search supports additional search methods that go beyond just a simple word search. From this search bar, you can incorporate some of the following:

- **Boolean operators -** You can use the basic Boolean operators ‘and’ or ‘or’ to refine your search. Note: Additional operators are not used within Exchange search.

  - OR - This allows the returned results to contain one term/word, the other, or both.
  - AND - This limits the returned results to *only* items whose information contains *both* terms or words.

- **Search specific filters -** You can specify a filter to limit search results to data matching that filter only. For example, you can return all raster data with this search: *type: raster*. Or you can look for data from a specific user: *owner: admin*.

- **Exclude specific criteria -** You can build a search that will exclude certain search criteria, as well. For example, if you wanted to search for the word ‘apples’, but *not* return anything that also contains the word `oranges`, you would use, *apples - oranges* or *apples not oranges*.

  .. figure:: img/content-search.png

Discover the Available Content
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In Exchange, your data is separated into multiple categories based on the content of the information. Your Exchange administrator can configure your datasets and metadata based on your settings and requirements. When searching for data, selecting on one of these available datasets will help you find information faster by returning only those results meeting the category criteria.

  .. figure:: img/discover-content.png

  *This is an example of what the content datasets could be for your Boundless Exchange instance. The specific datasets will depend on your settings and requirements.*

Featured Content
----------------

Featured datasets are available on the Boundless Exchange homepage, and allow users to immediately see maps, layers or documents which have been highlighted as important. A dataset can be featured by editing its metadata, and ensuring the Featured checkbox is selected.

  .. figure:: img/featured-content.png

Exploring
---------

**Layers** - To open the Explore Layers page, click on the Data link on the Boundless Exchange toolbar, and select Layers in the drop-down menu. Here you can browse data that has been uploaded into Exchange. Selecting on the View Details link will take you to the information page where you can download the layer, edit metadata, or view additional information about the layer.

**Maps** - To open the Explore Maps page, click on the Maps link on the Boundless Exchange toolbar, and select Explore Maps. Like the Layers page, the Maps page lets you browse the available maps that have been created in Exchange. Similar to a layer, selecting on the View Details link will take you to its information page.

**Documents** - To open the Explore Documents page, click on the Data link on the Boundless Exchange toolbar, and select Documents in the drop-down menu. From here, you can browse through all of the documents that have been uploaded into Exchange.

Filtering
^^^^^^^^^

All of the content added to Exchange can be filtered to help you better manage the data. Similar to data set categories, filters can be configured by an Exchange administrator to include additional, site specific options. Listed below are several options to refine your search results.

  * **Filter by Text** - Filters results using basic search terms. Type your search terms in the text box, and select your results from the displayed list. Multiple terms can be used, separated by ‘and’ or ‘or’.

   .. figure:: img/text-filter.png

  * **Filter by Category** - When content is added to Exchange, the user will select a category that best represents what is being added. This is reflected in the Categories panel, and allows other users to refine their search by looking for content belonging to that particular category. Your content can be added to the categories created in your settings:

   .. figure:: img/metadata-category.png

    *This is an example of what the categories will look like. They will correspond with the available datasets from the homepage, but may differ among Exchange instances.*

  When filtering, select on a category to limit the results list to the content tagged with that category title. Selecting another available category expands your results to include those layers in the results list. Click on the category a second time to remove it from the layer results list. Active filters will display in blue.

   .. figure:: img/category-filter-resize.png

  * **Filter by Type** - You can filter by the type of content added to Exchange.

   .. figure:: img/type-filter1.png

  * **Filter by Host** - Select registry layers and remote services based on where the data is hosted. This may be useful if you are looking for data from a specific organization.

   .. figure:: img/host-filter1.png

  * **Filter by Keywords** - If a user has associated keywords to the layer in the metadata, you can filter layers by those terms. Select on a keyword to limit results to those layers with associated keywords.

   .. figure:: img/keywords-filter1.png

  * **Filter by Owner** - You can select data based on the owner of the product. This may be useful if you are trying to quickly find products created by individuals on a joint project.

   .. figure:: img/filter-owners.png

  * **Filter by Date** - This will limit the list of products by a date range. In the Date panel, select the start date and the end date for the date range. The list will update to reflect those layers, documents or maps created within that timeframe.

  To find layers which have been Time Enabled, select the **Yes** checkbox to eliminate layers from your search that do not have time enabled attributes.

   .. figure:: img/date-filter.png

  * **Filter by Extent** - Zoom in and out to find products pertaining only to the extent displayed on the map.

   .. figure:: img/filter-extent.png
