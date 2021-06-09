# GANs-Evaluation
This GUI application is for subjectively evaluating  of generated images quality.
Evaluation images need to save in pickle file.<br>


# How to Evaluate
Download a picklefile.<br>
Generated image pickle file : https://drive.google.com/open?id=11Ag3Mc-W0xvYjISSAXMX5qlZqb3BYk56
```sh
unzip pickle-files.zip
./Evaluation.sh
```

1.Please, typing evaluator name on the entry box.  Then, click the insert button next to the entry box, after that displayed two images.<br>
2.Choose the radio button under the images. Consider whether the image corresponds to the condition and the image is clearness.<br>
If both image is not clearness and corresponding condition, click the Skip Button.<br>

When the first evaluation (DCGAN) is completed, the second evaluation (PGGAN) is automatically started.

<img width="363" alt="evalutation-exp" src="https://user-images.githubusercontent.com/27120804/40094429-ec393c90-5901-11e8-9585-5fe2580e2c3a.png">

# Requirement
over   : python2

PIL    : 1.1.7

pillow : over 3.0.0
