## Introduction
In this project we want to train a model with music composed by human musicians and generate new fragments of music with such a pre-trained model. Ideally, this fragment should be composed of multi-track instruments and form a rich enough, long enough melody and gain high score in user study .

In the base of [MuseGAN](https://salu133445.github.io/musegan/), we try a new loss function: [Relativistic loss](https://arxiv.org/abs/1807.00734) and get better performance.  

The training data is collected from
[Lakh Pianoroll Dataset](https://salu133445.github.io/lakh-pianoroll-dataset/)
to generate pop song phrases consisting of bass, drums, guitar, piano and
strings tracks.

Sample results are available in folder result.

## Prerequisites

> __Below we assume the working directory is the repository root.__

### Install dependencies

- Using pip

  ```sh
  # Install the dependencies
  pip install -r requirements.txt
  ```

## Scripts
 - train the model:

     ```sh
     # Train the model
     ./scripts/run_train.sh "./exp/my_experiment/" "0"
     ```

### Use pretrained models

1. Pretrained models are saved in exp
2. Perform inference from a trained model:

   ```sh
   # Run inference from a pretrained model
   ./scripts/run_inference.sh "./exp/default/" "0"
   ```

## Outputs

The generated pianorolls are stored in .npz format to save space and processing
time. You can use the following code to write them into MIDI files.

```python
from pypianoroll import Multitrack

m = Multitrack('./test.npz')
m.write('./test.mid')
```

