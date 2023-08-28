# Practical question

MOCCA is currently tested on real-world data from the lab to fix possible bugs. When investigating a cross-coupling reaction, unexpected elution times were observed for some of the peaks. It is thought that this could be due to a bug in the data parsing function.

It is known that dominant peaks on the chromatogram are:

    * starting material at 0.82 mins

    * second starting material at 0.97 mins
    
    * product at 1.12 mins

### Useful information

The version of MOCCA that you should be using can be cloned from [this github repo](https://github.com/HaasCP/mocca).

The chromatogram data can be loaded using:

```
from mocca.dad_data.apis.empower import read_empower
data, time, wavelength = read_empower('sample1.arw')
```

You are given two chromatograms of the same reaction, which were however recorded by different scientists. The data from `sample1.arw` seems to be just fine, but the peaks from `sample2.arw` have unexpected elution times.

If you installed everything correctly, the script `test.py` should run and show the chromatogram data. Note that this is a minimal example and not production code.

### Your task

1. Find the bug in the code and understand why are the elution times different than expected
2. Rewrite or fix the code so that it works
3. Optionaly, you can also optimize the code for speed. Currently, loading the file seems to take around 1 second, it should be possible to load the file under 300 ms (the exact times of course depend on your machine)

When writing the code, remember to make it well documented, clear and maintainable.

