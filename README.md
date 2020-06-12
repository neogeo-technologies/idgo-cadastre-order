# IDGO CADASTRE ORDER

## Configuration

Dans le fichier **settings.py** de l'application :

* Ajouter l'application :

    ```
    INSTALLED_APPS = [
        # ...
        'idgo_admin',
        'idgo_cadastre_order',
        # ...
    ]
    ```

Dans le fichier **urls.py** de l'application :

* Ajouter le _pattern_ :

    ```
    urlpatterns = [
        # ...
        url(),
        # ...
    ]
    ```
