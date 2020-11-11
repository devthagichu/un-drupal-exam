# UN Drupal Example Theme

## Create your project

- [ ] Create a local project folder

- [ ] Create your project in this folder (using Composer) from:
      https://github.com/drupal-composer/drupal-project.

## Set up your local dev environment

- [ ] Open Dev Desktop
- [ ] Select "Start with an existing Drupal site located on my computer"
- [ ] Set your "Local codebase folder" to the /web folder in the project you
      created above
- [ ] Set your "Local site name"
- [ ] Set the PHP version to 7.3
- [ ] Select "Create a new database", and set a name
- [ ] Click OK
- [ ] Go to your "Local site" URL in browser and install the site with the
      Standard installation profile

## Repository

- [ ] Create a repository for your project on Github.com.
- [ ] Commit your project to the repository.

## Languages

- [ ] Install the other official UN languages (Arabic, Chinese, French, Russian
      and Spanish).

## Theme

- [ ] Install the Bootstrap theme.
- [ ] Create a custom sub-theme of Bootstrap.

## Landing page

- [ ] Build a landing page (use www.unhabitat.org/old as a source/reference) with
      the features below.
- [ ] Install modules and create content types as needed, and feel free to apply your own design.

Use the Devel modules to generate dummy content.

- [ ] UN-Habitat logo
- [ ] Search box
- [ ] Language switcher
- [ ] Navigation/menu bar
- [ ] News Carousel/Slider/Slideshow (with image, title, date, and summary)
- [ ] News and Stories listing (with image and title)
- [ ] Video listing (with embedded YouTube videos)
- [ ] Tabbed display as seen on unhabitat.org/old
- [ ] Footer menu

## Other

- [ ] Create a captcha-protected Contact form.

## Custom development

### Module

### Create a custom module that:

- [ ] Generates a visualisation (chart/graph) of the number of nodes of each
      content type on the site.
- [ ] Provide a block that renders the chart.
- [ ] Caches the block and invalidates the cache once a week.

## Theme

- [ ] Implement the "Roboto" Google font as the default font .
- [ ] Add a custom region to your sub-theme that will contain the
      visualisation block you created above.
- [ ] Place this region/block at the bottom of the landing page.
- [ ] Override the 404 (Page not found) page to show a custom message and a
      search box.
- [ ] Create a theme setting to allow the 404 message to be specified in your
      sub-theme’s settings page.

## Configuration Management

- [ ] Using the "Configuration Split" module, create 2 separate configuration
      profiles:
- [ ] Development - [ ] This will have the complete site configuration
- [ ] Production - [ ] This should have the Devel, Views UI, Menu UI and Field
      UI modules disabled.
- [ ] Export the site configuration.

## Deployment

- [ ] Make a dump of your database.
- [ ] Commit the database dump and all your code and configuration to your
      repository.
- [ ] Compress the sites/default/files directory and commit it to your
      repository.
- [ ] Push your repository to Github.

## Report

Your repository URL:
