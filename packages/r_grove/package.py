# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGrove(RPackage):
	"""Wavelet Functional ANOVA Through Markov Groves

	Functional denoising and functional ANOVA through wavelet-domain 
  Markov groves. Fore more details see: Ma L. and Soriano J. (2018) 
  Efficient functional ANOVA through wavelet-domain Markov groves. 
  <arXiv:1602.03990v2 [stat.ME]>.
	"""
	
	cran = "grove" 

	version("1.1.1", md5="a48fad118a1d31ed19b282ba25bf427d")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-wavethresh", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
