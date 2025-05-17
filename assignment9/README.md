.venv\Scripts\activate

### Task 1: Review robots.txt to Ensure Policy Compliance
Verified. 

### Task 2: Understanding HTML and the DOM for the Durham Library Site
##### Task2a `<li class='row cp-search-result-item'>`
Find the HTML element for a single entry in the search results list. 

##### Task2b `<h2 class = 'cp-title'>`
Within that element, find the element that stores the title.  Note the tag type and the class value.  Your program will need this value too, so save it too.

##### Task2c `<h2 class="cp-title">` & `<span class="cp-author-link">`
Within the search results li element, find the element that stores the author.  Hint: This is a link.  Note the class value and save it.  Some books do have multiple authors, so you'll have to handle that case.

##### Task2d `<span class="display-info-primary">`
Within the search results li element, find the element that stores the format of the book and the year it was published.  Note the class value and save it.  Now in this case, the class might not be enough to find the part of the li element you want.  So look at the div element that contains the format and year.  You want to note that class value too.