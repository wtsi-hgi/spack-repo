# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSamprior(RPackage):
	"""Self-Adapting Mixture (SAM) Priors

	Implementation of the SAM prior and generation of its
     operating characteristics for dynamically borrowing information
     from historical data. For details, please refer to Yang et al. (2023)
     <doi:10.1111/biom.13927>. 
	"""
	
	cran = "SAMprior" 

	version("1.1.1", md5="c0aab2df8b87e8f944190e207a43e2f1")

	depends_on("r-rbest", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-metrics", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
