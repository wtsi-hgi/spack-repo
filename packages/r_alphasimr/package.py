# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAlphasimr(RPackage):
	"""Breeding Program Simulations

	The successor to the 'AlphaSim' software for breeding program 
  simulation [Faux et al. (2016) <doi:10.3835/plantgenome2016.02.0013>]. 
  Used for stochastic simulations of breeding programs to the level of DNA 
  sequence for every individual. Contained is a wide range of functions for 
  modeling common tasks in a breeding program, such as selection and crossing. 
  These functions allow for constructing simulations of highly complex plant and 
  animal breeding programs via scripting in the R software environment. Such 
  simulations can be used to evaluate overall breeding program performance and 
  conduct research into breeding program design, such as implementation of 
  genomic selection. Included is the 'Markovian Coalescent Simulator' ('MaCS') 
  for fast simulation of biallelic sequences according to a population 
  demographic history [Chen et al. (2009) <doi:10.1101/gr.083634.108>].
	"""
	
	homepage = "https://github.com/gaynorr/AlphaSimR"
	cran = "AlphaSimR" 

	version("1.5.3", md5="4d437649705f5dd3cc60206f155c0c3a")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
	depends_on("r-rcpparmadillo@0.7.500:", type=("build", "run"))
	depends_on("r-bh", type=("build", "run"))
