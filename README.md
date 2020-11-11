# UN Drupal Example Theme

## Create your project

- [x] Create a local project folder

- [x] Create your project in this folder (using Composer) from:
      https://github.com/drupal-composer/drupal-project.

## Set up your local dev environment

- [x] Open Dev Desktop
- [x] Select "Start with an existing Drupal site located on my computer"
- [x] Set your "Local codebase folder" to the /web folder in the project you
      created above
- [x] Set your "Local site name"
- [x] Set the PHP version to 7.3
- [x] Select "Create a new database", and set a name
- [x] Click OK
- [x] Go to your "Local site" URL in browser and install the site with the
      Standard installation profile

## Repository

- [x] Create a repository for your project on Github.com.
- [x] Commit your project to the repository.

## Languages

- [x] Install the other official UN languages (Arabic, Chinese, French, Russian
      and Spanish).

## Theme

- [x] Install the Bootstrap theme.
- [x] Create a custom sub-theme of Bootstrap.

## Landing page

- [x] Build a landing page (use www.unhabitat.org/old as a source/reference) with
      the features below.
- [x] Install modules and create content types as needed, and feel free to apply your own design.

Use the Devel modules to generate dummy content.

- [x] UN-Habitat logo
- [x] Search box
- [ ] Language switcher
- [x] Navigation/menu bar
- [x] News Carousel/Slider/Slideshow (with image, title, date, and summary)
- [x] News and Stories listing (with image and title)
- [x] Video listing (with embedded YouTube videos)
- [x] Tabbed display as seen on unhabitat.org/old
- [x] Footer menu

## Other

- [] Create a captcha-protected Contact form.

## Custom development

### Module

### Create a custom module that:

- [ ] Generates a visualisation (chart/graph) of the number of nodes of each
      content type on the site.
- [ ] Provide a block that renders the chart.
- [ ] Caches the block and invalidates the cache once a week.

## Theme

- [x] Implement the "Roboto" Google font as the default font .
- [x] Add a custom region to your sub-theme that will contain the
      visualisation block you created above.
- [x] Place this region/block at the bottom of the landing page.
- [ ] Override the 404 (Page not found) page to show a custom message and a
      search box.
- [ ] Create a theme setting to allow the 404 message to be specified in your
      sub-theme’s settings page.

## Configuration Management

- [x] Using the "Configuration Split" module, create 2 separate configuration
      profiles:
- [ ] Development \* [x] This will have the complete site configuration
- [ ] Production \* [x] This should have the Devel, Views UI, Menu UI and Field
      UI modules disabled.
- [x] Export the site configuration.

## Deployment

- [x] Make a dump of your database.
- [x] Commit the database dump and all your code and configuration to your
      repository.
- [x] Compress the sites/default/files directory and commit it to your
      repository.
- [x] Push your repository to Github.

## Report

Your repository URL:
