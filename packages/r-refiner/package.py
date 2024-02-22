# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRefiner(RPackage):
	"""Reference Interval Estimation using Real-World Data

	Indirect method for the estimation of reference intervals using 
	Real-World Data ('RWD'). It takes routine measurements of diagnostic 
	tests, containing pathological and non-pathological samples as input 
	and uses sophisticated statistical methods to derive a model describing 
	the distribution of the non-pathological samples. This distribution can 
	then be used to derive reference intervals. Furthermore, the package 
	offers functions for printing and plotting the results of the algorithm. 
	See ?refineR for a more comprehensive description of the features. 
	Version 1.0 of the algorithm is described in detail in 'Ammer et al. (2021)' 
	<doi:10.1038/s41598-021-95301-2>. Additional guidance on the usage of 
	the algorithm is given in 'Ammer et al. (2023)' <doi:10.1093/jalm/jfac101>.
	"""
	
	cran = "refineR" 

	version("1.6.1", md5="d3cb6f2d5ba63a7dacdd255b1b72ad9f")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-ash", type=("build", "run"))
	depends_on("r-future", type=("build", "run"))
	depends_on("r-future-apply", type=("build", "run"))
