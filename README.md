# tvtk-doc.org on the Read The Docs.

[![tvtk-auto-update](https://github.com/getfem-doc/tvtk-doc-translations/workflows/tvtk-auto-update/badge.svg)](https://github.com/getfem-doc/tvtk-doc-translations/actions)
[![Documentation Status](https://readthedocs.org/projects/tvtk/badge/?version=latest)](https://tvtk.readthedocs.io/en/latest/?badge=latest) 
[![Contributor Covenant](https://img.shields.io/badge/Contributor%20Covenant-v2.0%20adopted-ff69b4.svg)](CODE_OF_CONDUCT.md)

This is a project to provide tvtk official documentation with multiple versions and multiple languages on Read The Docs site.

Current procedure is bit tricky because Read The Docs doesn't have a way to specify options for sphinx-build command.
conf.py files for each languages have 'language' and 'locale_dirs' values without having full copy of conf.py of sphinx doc. If we want to specify conf.py file that is out of source directory, we will use '-c' option for sphinx-build command. Unfortunately Read the Docs can't. If there are any better way, please let me know.

## URLs

* RTD project pages for Sphinx:

  * https://readthedocs.org/projects/tvtk/  (Master)
  * https://readthedocs.org/projects/tvtk-ja/

* Documentation pages for each languages:

  * https://tvtk.readthedocs.io/en/latest/
  * https://tvtk.readthedocs.io/ja/latest/

## How to setup a translated documentation project on RTD

Detail is here: https://docs.readthedocs.org/en/latest/localization.html#project-with-multiple-translations

Points are:

* We must have RTD projects for each languages.
* Each projects must have correct Language setting on "Settings" page.
* Master project has connections to each translated projects on "translations settings" page.


## How to update po files

```
sh ./locale/update.sh
```

After that, you should commit updated po files.


## How to add a language

1. add language to locale/update.sh:

   ```
   - rm -R ja
   - tx pull -l ja
   + rm -R ja de
   + tx pull -l ja,de
   ```

2. update po files

3. commit them

4. add new project on Read The Docs like:

   https://readthedocs.org/projects/tvtk-ja/

5. add translation project to parent project like:

   https://readthedocs.org/dashboard/tvtk/translations/


## How to add a new version

1. add tag `1.7`

   ```
   git tag 1.7
   ```

2. replace old version `1_7` with `1_8` in:

   - release.sh
   - .travis.yml

3. commit it and push them:

   ```
   git add release.sh .travis.yml
   git commit -m "add new version: 1.8"
   git push --tags
   ```

4. enable version 1.7 on RTD:

   https://readthedocs.org/projects/tvtk/versions/

