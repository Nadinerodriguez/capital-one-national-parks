<img src="capital-one-logo.png" style="width: 100%" />


# Capital One Software Engineering Summit (Summer 2019)

Submission for CapitalOne's Mindsumo [challenge](https://www.mindsumo.com/contests/national-park-api) to Build a Web App that serves as a National Park Service Information Kiosk.

## Tech Stack
**Backend:**
- [Django](https://www.djangoproject.com/)

**Frontend:**
- HTML/CSS/JavaScript
- [jQuery](https://jquery.com/)
- [Bootstrap](https://getbootstrap.com/)

**Libraries and APIs**
- [National Park API](https://www.nps.gov/subjects/developer/api-documentation.htm#/) to present national park information
- [Requests](https://2.python-requests.org/en/master/) to parse JSON data
- [LeafletJS](https://leafletjs.com/) for rendering park map in javascript
- [Mapbox](https://www.mapbox.com/) for providing map resources

## Walkthrough
**Home Page**
<img src="find-a-park.gif" /><br />

**Results Page**
<img src="search.gif" /><br />

**Detail Page**
<img src="detail.gif" /><br />

## Features Implemented
**Required:**
- [x] Filter
    - State
- [x] Search
    - Name
    - Keyword
- [x] List Details
    - Alerts
    - Articles
    - News Releases
    - Events
    - Places
    - Visitor centers
    - Campgrounds
    - Lesson plans
    - People

**Stretch:**
- [x] Map Visualizations
- [ ] NPS Relevant Symbols

## Challenges
- Some API endpoints are [broken](https://developer.nps.gov/api/v1/campgrounds?q=fort&api_key={API_KEY}&fields=images). Could have used image resources for campgrounds 
- Not sure how to implement data caching, this could help improve speeds from API calls
- Implementing search suggestions
- Some JSON data returned for some locations have a lot of empty fields. This makes the user experience a little jarring.
- Passing data to other pages using forms and passing form data to django python files
- Styling a sticky "Categories" section on detail page
- Style a footer that fixes to bottom of viewport when there is not enough content

## License 
Copyright 2019 Nadine Rodriguez

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

