# CDE
Introducing Competitive Mechanism to Differential Evolution for Numerical Optimization

## Abstract
This paper introduces a novel competitive mechanism into differential evolution (DE), presenting an effective DE variant named competitive DE (CDE). CDE features a simple yet efficient mutation strategy: DE/winner-to-best/1. Essentially, the proposed DE/winner-to-best/1 strategy can be recognized as an intelligent integration of the existing mutation strategies of DE/rand-to-best/1 and DE/cur-to-best/1. The incorporation of DE/winner-to-best/1 and the competitive mechanism provide new avenues for advancing DE techniques. Moreover, in CDE, the scaling factor F and mutation rate Cr are determined by a random number generator following a normal distribution, as suggested by previous research. To investigate the performance of the proposed CDE, comprehensive numerical experiments are conducted on CEC2017 and engineering simulation optimization tasks, with CMA-ES, JADE, and other state-of-the-art optimizers and DE variants employed as competitor algorithms. The experimental results and statistical analyses highlight the promising potential of CDE as an alternative optimizer for addressing diverse optimization challenges.

## Citation
@misc{Zhong:24,  
  title={Introducing Competitive Mechanism to Differential Evolution for Numerical Optimization},   
  author={Rui Zhong and Yang Cao and Enzhi Zhang and Masaharu Munetomo},  
  year={2024},  
  eprint={2406.05436},  
  archivePrefix={arXiv},  
  primaryClass={cs.NE},  
  url={https://arxiv.org/abs/2406.05436},   
  note={Accepted by The 30th Int'l Conf on Parallel and Distributed Processing Techniques and Applications (PDPTA'24)}
}

## Datasets and Libraries
CEC benchmarks are provided by the opfunu library and engineering problems are provided by the enoppy library.
