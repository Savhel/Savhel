<?php 

    //pour l'enregistrement 
    if (isset($_POST['valider'])) {
        if (!empty($_POST['password'])) {
        $password = password_hash($_POST['password'],PASSWORD_DEFAULT /*il y'en a plusieurs mais moi j'utilise celui-ci*/ );
        /*ici donc tu peux faire ton iinsert into bd et tu auras le mot de passe caché ou encrypter*/
        }
    }

    //pour la connexion 
    if (isset($_POST['valider'])) {
        if (!empty($_POST['password'])) {
            //ici tu verifies si les mots de passe sont les mêmes avant de faire le header('location') avec 
           if (password_verify($_POST['password'],PASSWORD_DEFAULT)) {
                header('location : .........');
           }
        }
    }