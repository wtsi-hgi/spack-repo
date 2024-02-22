# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMrs(RPackage):
	"""Multi-Resolution Scanning for Cross-Sample Differences

	An implementation of the MRS algorithm for comparison across distributions,
  as described in Jacopo Soriano, Li Ma (2017) <doi:10.1111/rssb.12180>. 
  The model is based on a nonparametric process taking the form of a Markov model 
  that transitions between a "null" and an "alternative" state 
  on a multi-resolution partition tree of the sample space. 
  MRS effectively detects and characterizes a variety of underlying differences. 
  These differences can be visualized using several plotting functions.
	"""
	
	cran = "MRS" 

	version("1.2.6", md5="c73890e29aee329d2460f91e3a57443d")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
