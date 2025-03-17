# -*- coding: utf-8 -*-
"""
Created on Sat Mar 15 01:21:31 2025

@author: eliof
"""

import RPi.GPIO as GPIO
import time

# Définir les broches GPIO pour les LEDs et le buzzer
LED_BLEUE_PIN = 21
LED_ROUGE_PIN = 20
BUZZER_PIN = 26

# Fréquence et durée du bip sonore
FREQUENCE_BIP = 1000  # Fréquence du bip en Hz (1000 Hz = aigu)
DUREE_BIP = 0.5       # Durée du bip en secondes

# Initialisation des GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_BLEUE_PIN, GPIO.OUT)
GPIO.setup(LED_ROUGE_PIN, GPIO.OUT)
GPIO.setup(BUZZER_PIN, GPIO.OUT)  # Buzzer en mode sortie

# Fonction pour allumer une LED et éteindre l'autre
def controler_leds(plante_saine):
    if plante_saine:
        GPIO.output(LED_BLEUE_PIN, GPIO.HIGH)  # Allumer la LED bleue
        GPIO.output(LED_ROUGE_PIN, GPIO.LOW)   # Éteindre la LED rouge
        print("Plante saine : LED bleue allumée")
    else:
        GPIO.output(LED_BLEUE_PIN, GPIO.LOW)   # Éteindre la LED bleue
        GPIO.output(LED_ROUGE_PIN, GPIO.HIGH)  # Allumer la LED rouge
        print("Plante malade : LED rouge allumée")

# Fonction pour émettre un bip sonore
def emettre_bip():
    print("Émission d'un bip sonore")
    # Créer un signal PWM pour le buzzer
    pwm = GPIO.PWM(BUZZER_PIN, FREQUENCE_BIP)  # Fréquence du bip
    pwm.start(50)  # Démarrer le PWM avec un rapport cyclique de 50%
    time.sleep(DUREE_BIP)  # Garder le bip actif pendant la durée définie
    pwm.stop()  # Arrêter le PWM

ind = [3,5,7,11,15,18,20,23,24,25,28,38]

def LED(pred):
    plante_saine = False
    global ind
    # Attendre que le bouton soit pressé
    for i in ind:
        if pred == i:
            plante_saine = True
            break
        else : 
            plante_saine = False
    controler_leds(plante_saine)
    
    emettre_bip()
    time.sleep(1)

    GPIO.output(LED_BLEUE_PIN, GPIO.LOW)
    GPIO.output(LED_ROUGE_PIN, GPIO.LOW)
    print("LEDs off")


    time.sleep(0.1)  # Pour éviter la surcharge du CPU

