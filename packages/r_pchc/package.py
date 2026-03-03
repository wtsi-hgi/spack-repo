# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPchc(RPackage):
	"""Bayesian Network Learning with the PCHC and Related Algorithms

	Bayesian network learning using the PCHC algorithm. PCHC stands for PC Hill-Climbing, a new hybrid algorithm that uses PC to construct the skeleton of the BN and then 
			 applies the Hill-Climbing greedy search. More algorithms and variants have been added, such as MMHC, FEDHC, and the Tabu search variants, PCTABU, MMTABU and FEDTABU. 
			 The relevant papers are:
			 a) Tsagris M. (2021). A new scalable Bayesian network learning algorithm with applications to economics. Computational Economics, 57(1): 341-367. <doi:10.1007/s10614-020-10065-7>. 
			 b) Tsagris M. (2022). The FEDHC Bayesian Network Learning Algorithm. Mathematics 2022, 10(15): 2604. <doi:10.3390/math10152604>.
	"""
	
	cran = "pchc" 

	version("1.2", md5="786e006d641bbc53f9a8fe2a9c35acd9")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-bigstatsr", type=("build", "run"))
	depends_on("r-bnlearn", type=("build", "run"))
	depends_on("r-dcov", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-rfast", type=("build", "run"))
	depends_on("r-rfast2", type=("build", "run"))
	depends_on("r-robustbase", type=("build", "run"))
