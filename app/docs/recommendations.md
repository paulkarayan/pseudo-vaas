# Recommendations API

Convert Text into Images
---------
Returns a list of Shutterstock URLs based on keywords that are extracted from provided text. Keywords are extracted
from the body of text determined by which extractor is used.

### Fields
`extractor`:
* `monkey_learn`: Uses models from Monkey Learn apis to extract keywords
* `shutterstock`: Uses models from Shutterstock apis to extract keywords. (Default if no extractor is provided)
`text`: body oy text to search

`POST /recommendations/text_to_images`

```json
{
  "extractor": "monkey_learn",
  "text": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labor in"
}
```

#### Responses
```json
{
   "adipiscing":[
      "https://www.shutterstock.com/image-photo/1715604202",
      "https://www.shutterstock.com/image-photo/1868581786"
   ],
   "incididunt":[
      "https://www.shutterstock.com/image-photo/1723893052",
      "https://www.shutterstock.com/image-photo/1897779562"
   ]
}
```
