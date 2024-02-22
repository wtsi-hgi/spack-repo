# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIccforest(RPackage):
	"""An Ensemble Method for Interval-Censored Survival Data

	Implements the conditional inference forest approach 
  to modeling interval-censored survival data. It also provides 
  functions to tune the parameters and evaluate the model fit. See 
  Yao et al. (2019) <arXiv:1901.04599>.
	"""
	
	cran = "ICcforest" 

	version("0.5.1", md5="5ddfeea5d0c85e6c4c2561d96a0ebfb7")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-partykit", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-icenreg", type=("build", "run"))
	depends_on("r-ipred", type=("build", "run"))
