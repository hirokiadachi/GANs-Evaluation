# GANs-Evaluation
Subjective evaluation of generated images.<br>
Evaluation images need to save in pickle file.<br>


# How to Evaluate
Download a picklefile.<br>
Generated image pickle file : https://drive.google.com/open?id=11Ag3Mc-W0xvYjISSAXMX5qlZqb3BYk56
```sh
unzip pickle-files.zip
./Evaluation.sh
```

1.Type name on Entry Box.  Then, click the Enter Button next the Entry Box so be displayed two images.<br>
2.Choose the Radio Button under images.　Consider whether the image corresponds to the condition and the image is clearness.<br>
If both image is not clearness and corresponding condition, click the Skip Button.<br>

When the first evaluation (DCGAN) is completed, the second evaluation (PGGAN) is automatically started.

<img width="363" alt="evalutation-exp" src="https://user-images.githubusercontent.com/27120804/40094429-ec393c90-5901-11e8-9585-5fe2580e2c3a.png">

# Requirement
over   : python2

PIL    : 1.1.7

pillow : over 3.0.0
