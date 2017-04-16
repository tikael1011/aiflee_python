# aiflee_python
python code for aiflee to process raw data, written in Python 3.5.2

[![Python 3.5.2](https://img.shields.io/shippable/5444c5ecb904a4b21567b0ff.svg)]()
in order to avoid conflict with Numpy, some notation was altered


n_steps_results means given n input data (n > 1),output the location based on all inputs. n steps are continous, e.g. the first input is h1.10 than the second input is either h1.9 or h1.11. Mathematically,  'h1.10 then h1.11' (step forward) and  'h1.11 then h1.10' (step back) will have the same output.
