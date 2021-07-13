dictionary_ = {'info_name':   ["Software creato da Tommaso Bocchietti",
                               "Software created by Tommaso Bocchietti",
                               "Sooftware créé par Tommaso Bocchietti"],

               'info_text_1': ["Avrai bisogno di una stampante controllata da Arduino come quella nella foto",
                               "You will need an Arduino-controlled printer like the one in the picture",
                               "Vous aurez besoin d'une imprimante contrôlée par Arduino comme celle de l'image"],

               'info_text_2': ["N.B. Navigando tra vari menù puoi trovare link utili al progetto",
                               "Please note: by browsing through menus you can find useful links for the project",
                               "N.B. en naviguant entre les différents menus, vous pouvez trouver des liens utiles pour le projet"],

               'config_text_0': ["\nConfigura la tua stampante\n\n\n1. Inserisci la porta alla quale è collegata la scheda Arduino:",
                                 "\nSet up your printer\n\n\n1. Enter the port to which the Arduino board is connected:",
                                 "\nConfigurez votre imprimante\n\n\n1. Entrez le port auquel la carte Arduino est connectée:"],

               'config_text_1': ["2. Scarica la libreria 'AFmotor.h' (link nel menu)",
                                 "2. Download the library 'AFmotor.h' (link in the menu)",
                                 "2. Téléchargez la librairie 'AFmotor.h' (lien dans le menu)"],

               'config_text_2': ["3. Fai l'upload del seguente codice sulla tua scheda Arduino",
                                 "3. Upload the following code to your Arduino board",
                                 "3. Chargez le code suivant sur votre carte Arduino"],

               'config_save_code': ["Salva l'intero codice",
                                    "Save the entire code",
                                    "Sauvez le code entier"],

               'calibration_setting_text_0': ["Calibra l'altezza della penna (0/180)",
                                              "Calibrate the pen height (0/180)",
                                              "Calibrez la hauteur du stylo (0/180)"],

               'calibration_setting_text_1': ["Penna su:",
                                              "Pen up:",
                                              "Stylo en haut:"],

               'calibration_setting_text_2': ["Penna giù:",
                                              "Pen down:",
                                              "Stylo en bas:"],

               'calibration_setting_text_3': ["Controlla la direzione dei movimenti",
                                              "Control the movement direction",
                                              "Contrôlez la direction du mouvement"],

               'calibration_setting_text_4': ["Direzione asse X:",
                                              "X axis direction:",
                                              "Direction axe X:"],

               'calibration_setting_text_5': ["Direzione asse Y:",
                                              "Y axis direction:",
                                              "Direction axe Y:"],

               'calibration_setting_text_6': ["Porta manualmente la penna\nnella posizione del centrino rosso",
                                              "Manually bring the pen\nto the position of the red dot",
                                              "Amenez manuellement le stylo\nsur la position du point rouge"],

               'calibration_setting_load': ["Fai un test",
                                            "Run a test",
                                            "Effectuez un test"],

               'printimg_setting_text_0': ["Scegli l'immagine che vuoi stampare",
                                           "Choose the image you want to print",
                                           "Choisissez l'image que vous voulez imprimer"],

               'printimg_setting_selection': ["Apri file",
                                              "Open file",
                                              "Ouvrir le file"],

               'printimg_setting_text_1': ["Usa lo slider per regolare l'approssimazione\ndei contorni nell'immagine",
                                           "Use the slider to adjust the approximation\nof contours in the image",
                                           "Utilisez le slider pour ajuster l'approximation\ndu contour dans l'image"],

               'printimg_setting_filling': ["Modalità riempimento",
                                            "Filling mode",
                                            "Mode de remplissage"],

               'printimg_setting_go': ["Stampa!",
                                       "Print!",
                                       "Pressez!"],

               'printhand_setting_text_0': ["Usa la lavagna affianco per disegnare",
                                            "Use the board beside to draw",
                                            "Utilisez le tableau à côté pour dessiner"],

               'printhand_setting_text_1': ["Come utilizzarla:",
                                            "How to use it:",
                                            "Comment l'utiliser:"],

               'printhand_setting_text_2': ["- Clicca e trascina il cursore\n- Rimani all'interno del bordo nero",
                                            "- Click and drag the cursor\n- Stay within the black border",
                                            "- Cliquez et faites glisser le curseur\n- Restez à l'intérieur de la bordure noire"],

               'printhand_setting_text_3': ["Disegno e stampa saranno simultanei",
                                            "Drawing and printing will be simultaneous",
                                            "Le dessin et l'impression seront simultanées"],

               'printhand_setting_button_0': ["Ripulisci lavagna",
                                              "Clean up the board",
                                              "Nettoyez le tableau"],

               'printhand_setting_button_1': ["Salva lavagna (*.png)",
                                              "Save the board (*.png)",
                                              "Sauvez le tableau (*.png)"],

               'printtext_setting_text_0': ["Scrivi il testo ed imposta i parametri",
                                            "Write the text and set the parameters ",
                                            "Rédigez le texte et définissez les paramètres"],

               'printtext_setting_text_1': ["Carattere:",
                                            "Font menu",
                                            "Menu font"],

               'printtext_setting_text_2': ["Dimensione:",
                                            "Dimension:",
                                            "Dimension:"],

               'printtext_setting_text_3': ["Font:",
                                            "Font:",
                                            "Font:"],

               'printtext_setting_text_4': ["Paragrafo:",
                                            "Paragraph:",
                                            "Paragraphe:"],

               'printtext_setting_text_5': ["Rotazione pagina:",
                                            "Page rotation:",
                                            "Rotation de la page:"],

               'printtext_setting_button': ["Passa alla stampa!",
                                            "Go to print!",
                                            "Allez à la presse!"]
               }

align_o = [["Sinistra", "Centrato", "Destra"],
           ["Left", "Centred", "Right"],
           ["Gauche", "Centré", "Droit"]]

align_v = [["Alto", "Centrato", "Basso"],
           ["High", "Centred", "Low"],
           ["Haut", "Centré", "Bas"]]

direction_ = [["Positiva", "Negativa"],
              ["Positive", "Negative"],
              ["Positive", "Négative"]]

setConfig_ = [["Configurazione Arduino..", "Arduino configurato correttamente", "Arduino non trovato"],
              ["Arduino configuration..", "Arduino configured correctly", "Arduino not found"],
              ["Configuration de Arduino..", "Arduino configuré correctement", "Arduino non trouvé"]]

saveCode_ = [["Salva il codice", "Codice stampante Arduino"],
             ["Save the code", "Arduino printer code"],
             ["Sauvez le code", "Code d'imprimante Arduino"]]

setCalibr_ = [["Parametri iniziali per la stampante di Arduino. Non modificare il file.", "I parametri relativi alla penna devono essere compresi tra 0 e 180"],
              ["Initial parameters for the Arduino printer. Do not modify the file.", "The parameters for the pen must be between 0 and 180"],
              ["Paramètres initiaux pour l'imprimante Arduino. Ne pas modifier le fichier.", "Les paramètres du stylo doivent être compris entre 0 et 180"]]

openImg_ = ["Apri un immagine", "Open an image", "Ouvrez une image"]

saveCanvas_ = [["Salva la tua lavagna", "Lavagna Arduino"],
               ["Save your board", "Arduino board"],
               ["Sauvez votre tableau", "Tableau Arduino"]]

menu_ = [[["Informazioni", "Info", "Codice sorgente app", "Progetto stampante"], ["Configura", "Settaggio iniziale", "Libreria Arduino"], "Calibra", "Stampa immagine", "Disegna e stampa", "Scrivi e stampa"],
         [["Information", "Info", "App source code", "Printer project"], ["Configure", "Initial setup", "Arduino library"], "Calibrate", "Print image", "Draw and print", "Write and print"],
         [["Informations", "Info", "Code source de l'application", "Projet d'imprimante"], ["Configurez", "Réglage initial", "Librairie Arduino"], "Calibrez", "Imprimez l'image", "Dessinez et imprimez", "Écrivez et imprimez"]]

windows_ = ["GORLU la stampante!", "GORLU the printer!", "GORLU l'imprimante"]

loading_ = ["Caricamento...", "Loading...", "Loading..."]

error_msg = [["Errore..", "Passa a 'Configura' per ricollegare Arduino", "Passa a 'Calibra' per testare il settaggio iniziale"],
             ["Error..", "Switch to 'Configure' to reconnect the Arduino", "Switch to 'Calibrate' to test the initial setting"],
             ["Erreur..", "Passez à 'Configurez' pour reconnecter l'Arduino", "Passez à 'Calibrez' pour tester le réglage initial"]]

sub_windows_ = [["Interrompi", "Stampati %d su %d pixel totali\n%s"],
                ["Interrupt", "Printed %d out of %d total pixels\n%s"],
                ["Arrêter", "Imprimé %d sur %d pixels totaux\n%s"]]
