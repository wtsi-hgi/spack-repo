# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RXegapopulation(RPackage):
	"""Genetic Population Level Functions

	This collection of gene representation-independent functions 
   implements the population layer of extended evolutionary and genetic 
   algorithms and its support. The population layer consists of functions 
   for initializing, logging, observing, evaluating a population of genes, 
   as well as of computing the next population. For parallel evaluation of a 
   population of genes 4 execution models - named Sequential, MultiCore, 
   FutureApply, and Cluster - are provided. They are implemented by 
   configuring the lapply() function. The execution model FutureApply can be 
   externally configured as recommended by Bengtsson (2021) 
   <doi:10.32614/RJ-2021-048>. Configurable acceptance rules and cooling 
   schedules (see Kirkpatrick, S., Gelatt, C. D. J, and Vecchi, M. P. (1983) 
   <doi:10.1126/science.220.4598.671>, and Aarts, E., and Korst, J. 
   (1989, ISBN:0-471-92146-7) offer simulated annealing or greedy randomized 
   approximate search procedure elements. Adaptive crossover and mutation 
   rates depending on population statistics generalize the approach of 
   Stanhope, S. A. and Daida, J. M. (1996, ISBN:0-18-201-031-7). 
	"""
	
	homepage = "<https://github.com/ageyerschulz/xegaPopulation>"
	cran = "xegaPopulation" 

	version("1.0.0.0", md5="3c9864524333de74c01459afa0085020")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-future-apply", type=("build", "run"))
	depends_on("r-xegagagene", type=("build", "run"))
	depends_on("r-xegaselectgene", type=("build", "run"))
