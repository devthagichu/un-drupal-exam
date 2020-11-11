import os
import shutil
 



info = """
name: THEME_NAME
type: theme
description: "THEME_NAME is a custom theme developed for Un Drupal Exam by Thagichu Anthony"
core_version_requirement: ^8.8 || ^9
base theme: bootstrap_barrio
libraries:
  - THEME_NAME/global-styling
  - THEME_NAME/global-js

regions:
  bottom: Bottom  
  custom_region: Anthony Custom Region  
  header: Header
  menu: Main Menu
  hero: Main Hero
  content: Content
  calltoaction: calltoaction
  testimonial: testimonial
  sidebar: Sidebar
  footer: Footer
  footer1: Footer1
  footer2: Footer2
  footer3: Footer3
  footer4: Footer4
  copyright: copyright

"""
settings = """
disable_google_fonts: FALSE
"""
libraries = """
global-styling:
  version: VERSION
  css:
    theme:
      assets/css/main.css: {} 

global-js:
  version: VERSION
  js:
    assets/js/main.js: {} 
"""


def createDir(path, name):
    dir_path = os.path.join(path, name)
    os.mkdir(dir_path)
    print("Directory '% s' created" % dir_path)


def createInfo(theme_name, ext, content):
    parent_dir = os.getcwd()
    theme_dir = os.path.join(parent_dir, theme_name, theme_name)
    info_path = os.path.join(theme_dir,  theme_name+ext)
    f = open(info_path, "a")
    f.write(content)
    f.close()


def createFile(path,  content):
    f = open(path, "a")
    f.write(content)
    f.close()


def main(name):
    theme_name = name.replace(" ", "") + '_8_x'
    parent_dir = os.getcwd()
    createDir(parent_dir, theme_name)
    theme_dir = os.path.join(parent_dir, theme_name)
    createDir(theme_dir, theme_name)
    theme_path = os.path.join(theme_dir, theme_name)
    createDir(theme_path, "assets")
    createDir(theme_path, "templates")
    assets_path = os.path.join(theme_path, "assets")

    createDir(assets_path, "css")
    createDir(assets_path, "js")

    createFile(os.path.join(assets_path, "css", "main.css"), " ")
    createFile(os.path.join(assets_path, "js", "main.js"), " ")
    

    createInfo(theme_name, ".info.yml", info.replace("THEME_NAME", theme_name))
    createInfo(theme_name, ".libraries.yml", libraries)
    createInfo(theme_name, ".settings.yml", settings)

    shutil.make_archive(theme_name, 'zip', theme_dir)

    print("Theme '% s' created" % theme_name)


 

main("un_drupal_exam")
