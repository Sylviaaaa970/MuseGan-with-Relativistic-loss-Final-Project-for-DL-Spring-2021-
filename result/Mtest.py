import pypianoroll

m = pypianoroll.load('4/fake_x_bernoulli_sampling_24000.npz')
m.write('4/infer-24000.mid')
