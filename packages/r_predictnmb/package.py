# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPredictnmb(RPackage):
	"""Evaluate Clinical Prediction Models by Net Monetary Benefit

	Estimates when and where a model-guided treatment strategy may 
    outperform a treat-all or treat-none approach by Monte Carlo simulation and 
    evaluation of the Net Monetary Benefit. Details can be viewed in 
    Parsons et al. (2023) <doi:10.21105/joss.05328>.
	"""
	
	homepage = "https://docs.ropensci.org/predictNMB/"
	cran = "predictNMB" 

	version("0.2.1", md5="f5f11b3ce0eaa5444b588d92293a7d48")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-cutpointr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-pmsampsize", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
