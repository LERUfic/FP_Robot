#!/bin/bash

/usr/bin/python face_datasets.py
/usr/bin/python training.py
/usr/bin/python face_recognition.py
/bin/rm -rf trainer
/bin/rm -rf dataset
