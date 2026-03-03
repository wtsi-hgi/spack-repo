# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBlocksdesign(RPackage):
	"""Nested and Crossed Block Designs for Factorial and Unstructured
Treatment Sets

	Constructs treatment and block designs for linear treatment models
  with crossed or nested block factors. The treatment design can be any feasible 
  linear model and the block design can be any feasible combination of crossed or 
  nested block factors. The block design is a sum of one or more block factors
  and the block design is optimized sequentially with the levels of each successive
  block factor optimized conditional on all previously optimized block factors. 
  D-optimality is used throughout except for square or rectangular lattice block designs 
  which are constructed algebraically using mutually orthogonal Latin squares.
  Crossed block designs with interaction effects are optimized using a weighting scheme
  which allows for differential weighting of first and second-order block effects. 
  Outputs include a table showing the allocation of treatments to blocks and tables showing
  the achieved D-efficiency factors for each block and treatment design.  
  Edmondson, R.N. Multi-level Block Designs for Comparative Experiments. 
  JABES 25, 500–522 (2020) <doi:10.1007/s13253-020-00416-0>.
	"""
	
	homepage = "<doi:10.1007/s13253-020-00416-0>"
	cran = "blocksdesign" 

	version("4.9", md5="3b0bd8e593add5c97c57ef7a91600387")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-polynomf", type=("build", "run"))
