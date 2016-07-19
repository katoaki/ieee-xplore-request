# ieee-xplore-request

This shall be, in the future, a small script to automatically search the IEEE xplore database for relevant data. 
And scrape the relevant data from the html version of the articles.

This is a search script for the IEEE xplore database. It is intended to search basically for keywords in the actual journal papers and articles, so not all functionalities that are provided by the IEEE xplore are provided by this script. 

For all search possibilities of IEEE xplore see http://ieeexplore.ieee.org/gateway/

This script is all free, free to use, free to improve, but should kept as such after changing.

To do:
- include a header
- find out to get all the xml for all search results and not only the first 25 by default or up to 1000 if I'm smart enough to use the right search query 
	- there are the paging parameters, first request should find out how much search results we get. depending on that result "hc" numbers of records to fetch should be set appropriately. if results exceed 1000, "rs" sequence number of first record to fetch needs to be set accordingly.
- allow the user to use a variety of search types at the same time
- make the input failure safe, check if the input is valid and if not ask the user to input data again, think about a break condition
- how to work with xml data
- use the xml data to assemble the url for the html version of the article
- search the html website and download the relevant data: sentences with keywords, tables, figures
  - check the format of tables and figures
- decide how to save the data and a possible document/folder structure for it
  - if there is relevant data use the xml to assemble the bibtex data
