# ieee-xplore-request

This shall be, in the future, a small script to automatically search the IEEE xplore database for relevant data. 
And scrape the relevant data from the html version of the articles.

To do:
- include a header
- find out to get all the xml for all search results and not only the first 25 by default or up to 1000 if I'm smart enough to use the right search query
- allow the user to use a variety of search types at the same time
- make the input failure safe, check if the input is valid and if not ask the user to input data again, think about a break condition
- how to work with xml data
- use the xml data to assemble the url for the html version of the article
- search the html website and download the relevant data: sentences with keywords, tables, figures
  - check the format of tables and figures
- decide how to save the data and a possible document/folder structure for it
  - if there is relevant data use the xml to assemble the bibtex data
