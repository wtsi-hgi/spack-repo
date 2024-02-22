# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBkmr(RPackage):
	"""Bayesian Kernel Machine Regression

	Implementation of a statistical approach 
  for estimating the joint health effects of multiple 
  concurrent exposures, as described in Bobb et al (2015) 
  <doi:10.1093/biostatistics/kxu058>.
	"""
	
	homepage = "https://github.com/jenfb/bkmr"
	cran = "bkmr" 

	version("0.2.2", md5="63f6b4c4a7661fb6ed922037e517bd02")

	depends_on("r@3.1.2:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-nlme", type=("build", "run"))
	depends_on("r-fields", type=("build", "run"))
	depends_on("r-truncnorm", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-tmvtnorm", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
