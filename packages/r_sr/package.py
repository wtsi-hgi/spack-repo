# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSr(RPackage):
	"""Smooth Regression - The Gamma Test and Tools

	Finds causal connections in precision data, finds lags and embeddings in 
  time series, guides training of neural networks and other smooth models, evaluates 
  their performance, gives a mathematically grounded answer to the over-training 
  problem.  Smooth regression is based on the Gamma test, which measures smoothness
  in a multivariate relationship.  Causal relations are smooth, noise is not.  
  'sr' includes the Gamma test and search techniques that use it. 
  References: Evans & Jones (2002) <doi:10.1098/rspa.2002.1010>, 
  AJ Jones (2004) <doi:10.1007/s10287-003-0006-1>.
	"""
	
	homepage = "https://smoothregression.com"
	cran = "sr" 

	version("0.1.0", md5="0654337c21dc7679aa1eec817d8d97fb")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-progress", type=("build", "run"))
	depends_on("r-rann", type=("build", "run"))
	depends_on("r-vdiffr", type=("build", "run"))
