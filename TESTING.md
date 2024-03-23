# Testing

> [!NOTE]  
> Return back to the [README.md](README.md) file.

## Real users
Brseaford24 - Partner - Testing: Created post, edited and deleted. Like and un-liked post. Created a comment, edit and delete.

rydy91@gmail - Friend - Testing: Created post, edited and deleted. Like and un-liked post. Created a comment, edit and delete.

## Code Validation

### HTML

I have used the recommended [HTML W3C Validator](https://validator.w3.org) to validate all of my HTML files.

| Directory | File | Screenshot | Notes |
| --- | --- | --- | --- |
| about | about.html | ![screenshot](documentation/validation/w3c-about.png) | |
| blog | comment_delete.html | ![screenshot](documentation/validation/w3c-comment-delete.png) | |
| blog | comment_edit.html | ![screenshot](documentation/validation/w3c-comment-edit.png) | |
| blog | work.html | ![screenshot](documentation/validation/w3c-work.png) | |
| blog | work_create.html | ![screenshot](documentation/validation/w3c-work-create.png) | |
| blog | work_delete.html | ![screenshot](documentation/validation/w3c-work-delete.png) | |
| blog | work_details.html | ![screenshot](documentation/validation/w3c-work-details.png) | |
| blog | work_edit.html | ![screenshot](documentation/validation/w3c-work-edit.png) | |
| contact | contact.html | ![screenshot](documentation/validation/w3c-contact.png) | |
| home | index.html | ![screenshot](documentation/validation/w3c-home.png) | |
| templates | base.html | ![screenshot](documentation/validation/w3c-base.png) | |
| templates | index.html | ![screenshot](documentation/validation/w3c-index.png) | |
| templates | signup.html/allauth | ![screenshot](documentation/validation/w3c-signup.png) | Known errors with allauth register page |
| templates | logout.html/allauth | ![screenshot](documentation/validation/w3c-signin.png) | |
| templates | login.html/allauth | ![screenshot](documentation/validation/w3c-signout.png) | |
| templates | 404.html | ![screenshot](documentation/validation/w3c-404.png) | |
| templates | 500.html | ![screenshot](documentation/validation/w3c-500.png) | |
| user_dashboard | profile.html | ![screenshot](documentation/validation/w3c-profile.png) | |
| user_dashboard | profile_comments.html | ![screenshot](documentation/validation/w3c-profile-comments.png) | |
| user_dashboard | profile_contact.html | ![screenshot](documentation/validation/w3c-profile-contact.png) | |
| user_dashboard | profile_likes.html | ![screenshot](documentation/validation/w3c-profile-likes.png) | |
| user_dashboard | profile_picture.html | ![screenshot](documentation/validation/w3c-profile-picture.png) | |
| user_dashboard | profile_posts.html | ![screenshot](documentation/validation/w3c-profile-post.png) | |

### CSS

I have used the recommended [CSS Jigsaw Validator](https://jigsaw.w3.org/css-validator) to validate all of my CSS files.

| Directory | File | Screenshot | Notes |
| --- | --- | --- | --- |
| static | style.css | ![screenshot](documentation/validation/w3c-css.png) | |

### Python

I have used the recommended [PEP8 CI Python Linter](https://pep8ci.herokuapp.com) to validate all of my Python files.

| Directory | File | CI URL | Screenshot | Notes |
| --- | --- | --- | --- | --- |
| about | urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/BenFash/RateTheWork/main/about/urls.py) | ![screenshot](documentation/validation/linter-about-url.png) | |
| about | views.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/BenFash/RateTheWork/main/about/views.py) | ![screenshot](documentation/validation/linter-about-views.png) | |
| blog | admin.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/BenFash/RateTheWork/main/blog/admin.py) | ![screenshot](documentation/validation/linter-blog-admin.png) | |
| blog | forms.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/BenFash/RateTheWork/main/blog/forms.py) | ![screenshot](documentation/validation/linter-blog-forms.png) | |
| blog | models.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/BenFash/RateTheWork/main/blog/models.py) | ![screenshot](documentation/validation/linter-blog-models.png) | |
| blog | urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/BenFash/RateTheWork/main/blog/urls.py) | ![screenshot](documentation/validation/linter-blog-urls.png) | |
| blog | views.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/BenFash/RateTheWork/main/blog/views.py) | ![screenshot](documentation/validation/linter-blog-views.png) | |
| contact | admin.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/BenFash/RateTheWork/main/contact/admin.py) | ![screenshot](documentation/validation/linter-contact-admin.png) | |
| contact | forms.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/BenFash/RateTheWork/main/contact/forms.py) | ![screenshot](documentation/validation/linter-contact-forms.png) | |
| contact | models.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/BenFash/RateTheWork/main/contact/models.py) | ![screenshot](documentation/validation/linter-contact-models.png) | |
| contact | urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/BenFash/RateTheWork/main/contact/urls.py) | ![screenshot](documentation/validation/linter-contact-urls.png) | |
| contact | views.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/BenFash/RateTheWork/main/contact/views.py) | ![screenshot](documentation/validation/linter-contact-views.png) | |
| home | urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/BenFash/RateTheWork/main/home/urls.py) | ![screenshot](documentation/validation/linter-home-urls.png) | |
| home | views.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/BenFash/RateTheWork/main/home/views.py) | ![screenshot](documentation/validation/linter-home-views.png) | |
|  | manage.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/BenFash/RateTheWork/main/manage.py) | ![screenshot](documentation/validation/linter-manage.png) | |
| rate_the_work | settings.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/BenFash/RateTheWork/main/rate_the_work/settings.py) | ![screenshot](documentation/validation/linter-settings.png) | |
| rate_the_work | urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/BenFash/RateTheWork/main/rate_the_work/urls.py) | ![screenshot](documentation/validation/linter-urls.png) | |
| user_dashboard | admin.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/BenFash/RateTheWork/main/user_dashboard/admin.py) | ![screenshot](documentation/validation/linter-dash-admin.png) | |
| user_dashboard | forms.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/BenFash/RateTheWork/main/user_dashboard/forms.py) | ![screenshot](documentation/validation/linter-dash-forms.png) | |
| user_dashboard | models.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/BenFash/RateTheWork/main/user_dashboard/models.py) | ![screenshot](documentation/validation/linter-dash-models.png) | |
| user_dashboard | urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/BenFash/RateTheWork/main/user_dashboard/urls.py) | ![screenshot](documentation/validation/linter-dash-urls.png) | |
| user_dashboard | views.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/BenFash/RateTheWork/main/user_dashboard/views.py) | ![screenshot](documentation/validation/linter-dash-views.png) | |

## Browser Compatibility

I've tested my deployed project on the main 3 browsers to check for compatibility issues.

| Browser | Home | Work | About | Contact | Signin | Signout | Work Details | Comment Edit | Comment Delete | Profile | Profile Picture | Your Comments | Your Posts | Your Likes | Profile Contact | Register | Work Delete | Work Edit | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Chrome | ![screenshot](documentation/browsers/browser-chrome-home.png) | ![screenshot](documentation/browsers/browser-chrome-work.png) | ![screenshot](documentation/browsers/browser-chrome-about.png) | ![screenshot](documentation/browsers/browser-chrome-contact.png) | ![screenshot](documentation/browsers/browser-chrome-signin.png) | ![screenshot](documentation/browsers/browser-chrome-logout.png) | ![screenshot](documentation/browsers/browser-chrome-workdetails.png) ![screenshot](documentation/browsers/browser-chrome-workdetails2.png) | ![screenshot](documentation/browsers/browser-chrome-commentedit.png) | ![screenshot](documentation/browsers/browser-chrome-commentdelete.png) | ![screenshot](documentation/browsers/browser-chrome-profile.png) | ![screenshot](documentation/browsers/browser-chrome-profilepic.png) | ![screenshot](documentation/browsers/browser-chrome-profileyourcomments.png) | ![screenshot](documentation/browsers/browser-chrome-profileyourposts.png)  | ![screenshot](documentation/browsers/browser-chrome-profileyourlikes.png) | ![screenshot](documentation/browsers/browser-chrome-profilecontact.png) | ![screenshot](documentation/browsers/browser-chrome-register.png) | ![screenshot](documentation/browsers/browser-chrome-workdelete.png) | ![screenshot](documentation/browsers/browser-chrome-workedit.png) | Works as expected |
| Firefox | ![screenshot](documentation/browsers/browser-firefox-home.png) | ![screenshot](documentation/browsers/browser-firefox-work.png) | ![screenshot](documentation/browsers/browser-firefox-about.png) | ![screenshot](documentation/browsers/browser-firefox-contact.png) | ![screenshot](documentation/browsers/browser-firefox-signin.png) | ![screenshot](documentation/browsers/browser-firefox-logout.png) | ![screenshot](documentation/browsers/browser-firefox-workdetails.png) ![screenshot](documentation/browsers/browser-firefox-workdetails2.png) | ![screenshot](documentation/browsers/browser-firefox-commentedit.png) | ![screenshot](documentation/browsers/browser-firefox-commentdelete.png) | ![screenshot](documentation/browsers/browser-firefox-profile.png) | ![screenshot](documentation/browsers/browser-firefox-profilepic.png) | ![screenshot](documentation/browsers/browser-firefox-profileyourcomments.png) | ![screenshot](documentation/browsers/browser-firefox-profileyourposts.png)  | ![screenshot](documentation/browsers/browser-firefox-profileyourlikes.png) | ![screenshot](documentation/browsers/browser-firefox-profilecontact.png) | ![screenshot](documentation/browsers/browser-firefox-register.png) | ![screenshot](documentation/browsers/browser-firefox-workdelete.png)| ![screenshot](documentation/browsers/browser-firefox-workedit.png) | Works as expected |
| Edge | ![screenshot](documentation/browsers/browser-edge-home.png) | ![screenshot](documentation/browsers/browser-edge-work.png) | ![screenshot](documentation/browsers/browser-edge-about.png) | ![screenshot](documentation/browsers/browser-edge-contact.png) | ![screenshot](documentation/browsers/browser-edge-signin.png) | ![screenshot](documentation/browsers/browser-edge-logout.png) | ![screenshot](documentation/browsers/browser-edge-workdetails.png) ![screenshot](documentation/browsers/browser-edge-workdetails2.png) | ![screenshot](documentation/browsers/browser-edge-commemtedit.png) | ![screenshot](documentation/browsers/browser-edge-commentdelete.png) | ![screenshot](documentation/browsers/browser-edge-profile.png) | ![screenshot](documentation/browsers/browser-edge-profilepic.png) | ![screenshot](documentation/browsers/browser-edge-profileyourcomments.png) | ![screenshot](documentation/browsers/browser-edge-profileyourposts.png)  | ![screenshot](documentation/browsers/browser-edge-profileyourlikes.png) | ![screenshot](documentation/browsers/browser-edge-profilecontact.png) | ![screenshot](documentation/browsers/browser-edge-register.png) | ![screenshot](documentation/browsers/browser-edge-workdelete.png) | ![screenshot](documentation/browsers/browser-edge-workedit.png) | Works as expected |

## Responsiveness

I've tested my deployed project on multiple devices to check for responsiveness issues using Devtools. 

| Device | Home | Work | About | Contact | Signin | Signout | Work Details | Comment Edit | Comment Delete | Profile | Profile Picture | Your Comments | Your Posts | Your Likes | Profile Contact | Register | Work Delete | Work Edit | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Mobile (DevTools) | ![screenshot](documentation/responsiveness/mobile-home.png) | ![screenshot](documentation/responsiveness/mobile-work.png) ![screenshot](documentation/responsiveness/mobile-work2.png) ![screenshot](documentation/responsiveness/mobile-work3.png) ![screenshot](documentation/responsiveness/mobile-work4.png) | ![screenshot](documentation/responsiveness/mobile-about.png) ![screenshot](documentation/responsiveness/mobile-about2.png) | ![screenshot](documentation/responsiveness/mobile-contact.png) ![screenshot](documentation/responsiveness/mobile-contact2.png) | ![screenshot](documentation/responsiveness/mobile-signin.png) | ![screenshot](documentation/responsiveness/mobile-signout.png) | ![screenshot](documentation/responsiveness/mobile-workdetails.png) ![screenshot](documentation/responsiveness/mobile-workdetails2.png) ![screenshot](documentation/responsiveness/mobile-workdetails3.png) ![screenshot](documentation/responsiveness/mobile-workdetails4.png) | ![screenshot](documentation/responsiveness/mobile-commentedit.png) | ![screenshot](documentation/responsiveness/mobile-commentdelete.png) | ![screenshot](documentation/responsiveness/mobile-profile.png) ![screenshot](documentation/responsiveness/mobile-profile2.png) | ![screenshot](documentation/responsiveness/mobile-profilepic.png) | ![screenshot](documentation/responsiveness/mobile-profileyourcomments.png) ![screenshot](documentation/responsiveness/mobile-profileyourcomments2.png) | ![screenshot](documentation/responsiveness/mobile-profileyourposts.png) ![screenshot](documentation/responsiveness/mobile-profileyourposts2.png) | ![screenshot](documentation/responsiveness/mobile-profileyourlikes.png) ![screenshot](documentation/responsiveness/mobile-profileyourlikes2.png) ![screenshot](documentation/responsiveness/mobile-profileyourlikes3.png) | ![screenshot](documentation/responsiveness/mobile-profilecontact.png) | ![screenshot](documentation/responsiveness/mobile-register.png) | ![screenshot](documentation/responsiveness/mobile-workdelete.png) | ![screenshot](documentation/responsiveness/mobile-workedit.png) ![screenshot](documentation/responsiveness/mobile-workedit2.png) | Works as expected |
| Tablet (DevTools) | ![screenshot](documentation/responsiveness/tablet-home.png) | ![screenshot](documentation/responsiveness/tablet-work.png) ![screenshot](documentation/responsiveness/tablet-work2.png) | ![screenshot](documentation/responsiveness/tablet-about.png) | ![screenshot](documentation/responsiveness/tablet-contact.png) | ![screenshot](documentation/responsiveness/tablet-signin.png) | ![screenshot](documentation/responsiveness/tablet-signout.png) | ![screenshot](documentation/responsiveness/tablet-workdetails.png) ![screenshot](documentation/responsiveness/tablet-workdetails2.png) | ![screenshot](documentation/responsiveness/tablet-commentedit.png) | ![screenshot](documentation/responsiveness/tablet-commentdelete.png) | ![screenshot](documentation/responsiveness/tablet-profile.png) | ![screenshot](documentation/responsiveness/tablet-profilepic.png) | ![screenshot](documentation/responsiveness/tablet-profileyourcomments.png) | ![screenshot](documentation/responsiveness/tablet-profileyourposts.png) | ![screenshot](documentation/responsiveness/tablet-profileyourlikes.png) ![screenshot](documentation/responsiveness/tablet-profileyourlikes2.png) | ![screenshot](documentation/responsiveness/tablet-profilecontact.png) | ![screenshot](documentation/responsiveness/tablet-register.png) | ![screenshot](documentation/responsiveness/tablet-workdelete.png) | ![screenshot](documentation/responsiveness/tablet-workedit.png) | Works as expected, edit button on your comments page sits close to "for work" line |
| Desktop (DevTools) | ![screenshot](documentation/responsiveness/desktop-home.png) | ![screenshot](documentation/responsiveness/desktop-work.png) | ![screenshot](documentation/responsiveness/desktop-about.png) | ![screenshot](documentation/responsiveness/desktop-contact.png) | ![screenshot](documentation/responsiveness/desktop-signin.png) | ![screenshot](documentation/responsiveness/desktop-signout.png) | ![screenshot](documentation/responsiveness/desktop-workdetails.png) ![screenshot](documentation/responsiveness/desktop-workdetails2.png) | ![screenshot](documentation/responsiveness/desktop-commentedit.png) | ![screenshot](documentation/responsiveness/desktop-commentdelete.png) | ![screenshot](documentation/responsiveness/desktop-profile.png) | ![screenshot](documentation/responsiveness/desktop-profilepic.png) | ![screenshot](documentation/responsiveness/desktop-profileyourcomments.png) | ![screenshot](documentation/responsiveness/desktop-profileyourposts.png) | ![screenshot](documentation/responsiveness/desktop-profileyourlikes.png) | ![screenshot](documentation/responsiveness/desktop-profilecontact.png) | ![screenshot](documentation/responsiveness/desktop-register.png) | ![screenshot](documentation/responsiveness/tablet-workdelete.png) | ![screenshot](documentation/responsiveness/desktop-workedit.png) ![screenshot](documentation/responsiveness/desktop-workedit2.png) | Works as expected |

## Lighthouse Audit

I've tested my deployed project using the Lighthouse Audit tool. Desktop scored better than mobile

| Page | Mobile | Desktop | Notes |
| --- | --- | --- | --- |
| Home | ![screenshot](documentation/lighthouse/lighthouse-home-mobile.png) | ![screenshot](documentation/lighthouse/lighthouse-home-desktop.png) | |
| Work | ![screenshot](documentation/lighthouse/lighthouse-work-mobile.png) | ![screenshot](documentation/lighthouse/lighthouse-about-desktop.png) | Longer loading times on performance to be expected due to large amount of user uploaded images |
| About | ![screenshot](documentation/lighthouse/lighthouse-about-mobile.png) | ![screenshot](documentation/lighthouse/lighthouse-about-desktop.png) | |
| Contact | ![screenshot](documentation/lighthouse/lighthouse-contact-mobile.png) | ![screenshot](documentation/lighthouse/lighthouse-contact-desktop.png) | |
| Work Details | ![screenshot](documentation/lighthouse/lighthouse-workdetails-mobile.png) | ![screenshot](documentation/lighthouse/lighthouse-workdetails-desktop.png) | |
| Comment Edit | ![screenshot](documentation/lighthouse/lighthouse-commentedit-mobile.png) | ![screenshot](documentation/lighthouse/lighthouse-commentedit-desktop.png) | |
| Comment Delete | ![screenshot](documentation/lighthouse/lighthouse-commentdelete-mobile.png) | ![screenshot](documentation/lighthouse/lighthouse-commentdelete-desktop.png) | |
| Profile | ![screenshot](documentation/lighthouse/lighthouse-profile-mobile.png) | ![screenshot](documentation/lighthouse/lighthouse-profile-desktop.png) | |
| Profile Picture | ![screenshot](documentation/lighthouse/lighthouse-profilepic-mobile.png) | ![screenshot](documentation/lighthouse/lighthouse-profilepic-desktop.png) | |
| Your Comments | ![screenshot](documentation/lighthouse/lighthouse-profileyourcomments-mobile.png) | ![screenshot](documentation/lighthouse/lighthouse-profileyourcomments-desktop.png) | |
| Your Posts | ![screenshot](documentation/lighthouse/lighthouse-profileyourposts-mobile.png) | ![screenshot](documentation/lighthouse/lighthouse-profileyourposts-desktop.png) | Longer loading times on performance to be expected due to large amount of user uploaded images |
| Your Likes | ![screenshot](documentation/lighthouse/lighthouse-profileyourlikes-mobile.png) | ![screenshot](documentation/lighthouse/lighthouse-profileyourlikes-desktop.png) | |
| Profile Contact | ![screenshot](documentation/lighthouse/lighthouse-profilecontact-mobile.png) | ![screenshot](documentation/lighthouse/lighthouse-profilecontact-desktop.png) | |
| Register | ![screenshot](documentation/lighthouse/lighthouse-register-mobile.png) | ![screenshot](documentation/lighthouse/lighthouse-register-desktop.png) | |
| Work Delete | ![screenshot](documentation/lighthouse/lighthouse-workdelete-mobile.png) | ![screenshot](documentation/lighthouse/lighthouse-workdelete-desktop.png) | |
| Work Edit | ![screenshot](documentation/lighthouse/lighthouse-workedit-mobile.png) | ![screenshot](documentation/lighthouse/lighthouse-workedit-desktop.png) | |
| 404 | ![screenshot](documentation/lighthouse/lighthouse-404-mobile.png) | ![screenshot](documentation/lighthouse/lighthouse-404-desktop.png) | |
| 500 | ![screenshot](documentation/lighthouse/lighthouse-500-mobile.png) | ![screenshot](documentation/lighthouse/lighthouse-500-desktop.png) | |

## Defensive Programming

Defensive programming was manually tested with the below user acceptance testing:

| Page | User Action | Expected Result | Pass/Fail | Comments |
| --- | --- | --- | --- | --- |
| Home | | | | |
| | Click on Logo | Redirection to Home page | Pass | |
| | Click on Home link in navbar | Redirection to Home page | Pass | |
| | Click on Work link in navbar | Redirection to Work page | Pass | |
| | Click on Login link in navbar | Redirection to Login page | Pass | |
| | Click on Register link in navbar | Redirection to Register page | Pass | |
| | Click on Logout link in navbar | Redirection to Logout page | Pass | |
| | Click on Profile link in navbar | Redirection to Profile page | Pass | |
| | Click on Profile picture in navbar | Redirection to Profile page | Pass | |
| | Click on Search in body | Presents results | Pass | |
| | Click on Pagination next in body | Presents next page | Pass | searched "hi" |
| | Click on Pagination previous in body | Presents previous page | Pass | |
| | Click on Social links in footer | All redirect to relevant sites  | Pass | |
| | Click on About us in footer | All redirect to About us page  | Pass | |
| | Click on Contact us in footer | All redirect to Contact us page  | Pass | |
| Work | | | | |
| | Click on Work link | Redirection to Work page | Pass | |
| | Click on Create Work link in body| Redirection to Create Work page | Pass | |
| | Click work cards | All cards load as expected | Pass | |
| | Click on Pagination next in body | Presents next page | Pass | |
| | Click on Pagination previous in body | Presents previous page | Pass | |
| | Logged out to see if create work button displayed | Did not | Pass | |
| Create Work | | | | |
| | Click on Create Work link | Redirection to Create Work page | Pass | |
| | Left Title field empty  | Required field prevents submit | Pass | |
| | Left Image field empty | Required field prevents submit | Pass | |
| | Left Catagories field empty | Required field prevents submit | Pass | |
| | Left Content field empty | Required field prevents submit | Pass | |
| | Left Sub-category field empty | Form submits as expected | Pass | |
| | Checked Admin to approve | Post did not show until admin approved | Pass | |
| | Click work cards | All cards load as expected | Pass | |
| | Click on Pagination next in body | Presents next page | Pass | |
| | Brute forcing the URL to get to this page whilst not signed in | Redirected to 404 | Pass | |
| Contact | | | | |
| | Click on Contact Us link | Redirection to Contact Us page | Pass 
| | Left Name field empty | Required field prevents submit | Pass | |
| | Left Subject field empty | Required field prevents submit | Pass | |
| | Left Email field empty | Required field prevents submit also requires email formatting inputted | Pass | |
| | Left Message field empty | Required field prevents submit | Pass | |
| | Click Submit | Form sends off to admin | Pass | |
| | Checked admin panel to see if received | Received | Pass | |
| | Intentionally broke contact form in html | Redirected to 500 | Pass | |
| Signin | | | | |
| | Click on the Login link | Redirection to Login page | Pass | |
| | Enter valid email address | Field will only accept email address format | Pass | |
| | Enter valid password | Field will only accept password format | Pass | |
| | Click Login button | Redirects user to home page | Pass | |
| Signout | | | | |
| | Click Logout button | Redirects user to logout page | Pass | Confirms logout first |
| | Click Confirm Logout button | Redirects user to home page | Pass | |
| Work Details  | | | | |
| | Click on any of the work cards from work page | Redirection relevant work | Pass | |
| | Non logged in user | Like and leave rating section not available | Pass | |
| | Logged in user | Like and leave rating section available | Pass | |
| | Logged in as user of work - Click on the Work Edit button. User redirected to the edit work page | Pass | |
| | Logged in as user of work- Click on the Work Delete button. User redirected to the delete work page | Pass | |
| | Logged in as another user | Edit work button not available | Pass | |
| | Logged in as another user  | Delete work button not available | Pass | |
| | Click leave a like button | Can leave a like and remove your like. Like total on page and card front update | Pass | |
| | Click leave a rating - with out content | Form does not submit due to required field| Pass | |
| | Click leave a rating - with out Suggested price | Form submit | Pass | |
| | Click leave a rating | Once submit comment does not show in rating until approval of admin | Pass | |
| | Log into admin panel to approve | Once approved comments shows in work details page ratings | Pass | |
| | Logged in as another user | Edit rating button not available | Pass | |
| | Logged in as another user | Delete rating button not available | Pass | |
| | Logged in as user of rating | Delete rating button available. User redirected to the delete work page | Pass | |
| | Logged in as user of rating| Delete rating button available. User redirected to the delete work page | Pass | |
| Ratings Edit | | | | |
| | Click Ratings edit button | Redirects user to edit rating page | Pass | |
| | Click Confirm Logout button | Redirects user to home page | Pass | |
| | Click Edit Comment rating - with out content | Form does not submit due to required field| Pass | |
| | Click leave a rating - with out Suggested price | Form submits | Pass | |
| | Log into admin panel to approve | Once approved comments shows in work details page ratings | Pass | |
| Ratings Delete | | | | |
| | Click Delete comment button | Redirects user to comment delete page | Pass | Confirms delete first |
| | Click Confirm delete button | Redirects user to work page | Pass | |
| Profile | | | | |
| | Non logged in user | Button in nav not available | Pass |  |
| | Click Profile button | Redirects user to profile page | Pass |  |
| | Non logged in user brute forcing the URL to get into profile section | Redirected to 404 page | Pass | |
| Profile Picture | | | | |
| | Click Profile picture button from profile page | Redirects user to profile picture page | Pass | 
| | Left image field empty | form submits | Pass | Placeholder profile picture shows in nav |
| | Left user type field empty | Form does not submit due to required field | Pass |  |
| | Insert image into field | form submits, redirect to profile page | Pass | Profile picture shows in nav |
| | Select clear current and submit | form submits, redirect to profile page | Pass | Placeholder profile picture shows in nav |
| | Select user type | Dropdown selection as expected | Pass | |
| | Non logged in user brute forcing the URL to get into profile section | User should be given an error | Pass | Error message presented |
| Your Comments | | | | |
| | Click Your comments button from profile page | Redirects user to your comments page | Pass | shows only users comments |
| | Click For works button | Redirects user to relevant work comment is for | Pass | |
| | Click For edit button | Redirects user to edit comment page for the relevant comment | Pass | |
| | Click For delete button | Redirects user to delete comment page for the relevant comment | Pass | |
| | Non logged in user should not see leave like and comment section | User cannot see this area | Pass | |
| Your Posts | | | | |
| | Click Your posts button from profile page | Redirects user to your posts page | Pass | shows only users posts |
| | Click any of the posts cards | Redirects user to relevant work details page | Pass | |
| | Non logged in user brute forcing the URL to get into profile  section | Redirected to 404 page | Pass | |
| Your Likes | | | | |
| | Click Your likes button from profile page | Redirects user to your likes page | Pass | shows only users liked posts |
| | Click any of the posts cards | Redirects user to relevant work details page | Pass | |
| | Non logged in user brute forcing the URL to get into profile  section | Redirected to 404 page | Pass | |
| Profile Contact | | | | |
| | Click Contact Admin button from profile page | Redirects user to contact admin page | Pass | |
| | Left Subject field empty | Required field prevents submit | Pass | |
| | Left Email field empty | Required field prevents submit also requires email formatting inputted | Pass | |
| | Left Message field empty | Required field prevents submit | Pass | |
| | Click Submit button | Redirects user to profile page | Pass | |
| | Log into admin panel to view | Form is available to read | Pass | |
| | Non logged in user brute forcing the URL to get into profile section | Redirected to 404 page | Pass |  |
| | Intentionally broke contact form in html | Redirected to 500 | Pass | |
| Register | | | | |
| | Click Register button | Redirects user to register page | Pass |  |
| | Left Email field empty | Required field prevents submit | Pass | |
| | Left Username field empty | Required field prevents submit | Pass | |
| | Left Password fields empty | Required field prevents submit | Pass | |
| | Click Sign up button | Creates account and redirects to home | Pass | |
| Work Delete | | | | |
| | Click Delete button | Redirects user to Delete Work page | Pass | Confirms delete first |
| | Click Confirm Delete button | Redirects user to work page and deletes relevant work | Pass | |
| Work Edit | | | | |
| | Click Work edit button | Redirects user to work edit page | Pass | Confirms edit first |
| | Left Title field empty  | Required field prevents submit | Pass | |
| | Left Image field empty | Required field prevents submit | Pass | |
| | Left Catagories field empty | Required field prevents submit | Pass | |
| | Left Content field empty | Required field prevents submit | Pass | |
| | Left Sub-category field empty | Form submits as expected | Pass | |
| | Checked Admin to approve | Post showed approved, post should go back to unapproved for monitoring | Pass | work.approved = False now added to view to prevent this |

## User Story Testing

| User Story | Screenshot |
| --- | --- |
| As a user I would like to be able to search for posts based on keywords or categories, so that I can find relevant content. | ![screenshot](documentation/feat/search.png) |
| As a user I would like to be able to view posts so that I can see works completed/received by the community. | ![screenshot](documentation/feat/viewpost.png) |
| As a user I would like to be able to contact admin so that I can provide feedback and suggestions. | ![screenshot](documentation/feat/usercontact.png) |
| As a user I would like to know that I am at the correct site so that I can be ensured im engaging with the correct community. | ![screenshot](documentation/feat/landingpage.png) |
| As a user I would like to sign up to the site so that I can make posts and comments. | ![screenshot](documentation/feat/register.png) |
| As a registered user I would like to be able to create a new post so that i can showcase my work/project in order to receive feedback from the community. | ![screenshot](documentation/feat/create-work.png) ![screenshot](documentation/feat/create-workform.png) |
| As a registered user I would like to comment on posts made by other users so that i can provide feedback and engage with the community. | ![screenshot](documentation/feat/comment-like.png) |
| As a registered user I would like to to be able to like posts made by other users so that i can provide quick feedback. | ![screenshot](documentation/feat/comment-like.png) |
| As a registered user I would like to be able to view my own posts so that i can keep track of my contributions to the platform. | ![screenshot](documentation/feat/yourposts.png) |
| As a registered user I would like to be able to edit and delete my comments so that i can amend them if i have made a mistake. | ![screenshot](documentation/feat/comment-editdelete.png) |
| As a registered user I would like to be able to edit and delete my posts so that i can edit and amend if needed. | ![screenshot](documentation/feat/post-editdelete.png) |
| As a registered user I would like to upload a profile picture so that i can add personality to my account. | ![screenshot](documentation/feat/uploadpic.png) |
| As a site administrator I would like to be able to approve posts and comments so that i can maintain a positive and respectful community environment. | ![screenshot](documentation/feat/approve-post.png) ![screenshot](documentation/feat/approve-comment.png) |
| As site administrator I would like to have a about page so that i can give users more info about the site. | ![screenshot](documentation/feat/about.png) |

## Bugs

### GitHub **Issues**

**Fixed Bugs**

[![GitHub issue custom search](https://img.shields.io/github/issues-search?query=repo%3ABenFash%2FRateTheWork%20label%3Abug&label=bugs)](https://github.com/BenFash/RateTheWork/issues?q=is%3Aissue+is%3Aclosed+label%3Abug)

All previously closed/fixed bugs can be tracked [here](https://github.com/BenFash/RateTheWork/issues?q=is%3Aissue+is%3Aclosed).

| Bug | Status |
| --- | --- |
| [Django - Auto like on posts](https://github.com/BenFash/RateTheWork/issues/17) | Closed |
| [Django - Auto suggested price fill on work create](https://github.com/BenFash/RateTheWork/issues/18) | Closed |
| [Django - Paginate not working on landing page(with search function)](https://github.com/BenFash/RateTheWork/issues/20) | Closed |
| [Django - Profile picture not loading](https://github.com/BenFash/RateTheWork/issues/19) | Closed |
| [Django - Fixing user being able to change their already uploaded profile picture](https://github.com/BenFash/RateTheWork/issues/21) | Closed |
| [Django - Brute forcing URLS](https://github.com/BenFash/RateTheWork/issues/22) | Closed |
| [Django - Post did not go not approved after edit](https://github.com/BenFash/RateTheWork/issues/23) | Closed |
| [CSS - Your comments edit and delete button](https://github.com/BenFash/RateTheWork/issues/24) | Closed |

**Open Issues**

[![GitHub issues](https://img.shields.io/github/issues/BenFash/RateTheWork)](https://github.com/BenFash/RateTheWork/issues)
[![GitHub closed issues](https://img.shields.io/github/issues-closed/BenFash/RateTheWork)](https://github.com/BenFash/RateTheWork/issues?q=is%3Aissue+is%3Aclosed)

Any remaining open issues can be tracked [here](https://github.com/BenFash/RateTheWork/issues).

## Unfixed Bugs

> [!NOTE]  
> There are no remaining bugs that I am aware of.
