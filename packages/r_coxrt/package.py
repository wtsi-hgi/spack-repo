# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCoxrt(RPackage):
	"""Cox Proportional Hazards Regression for Right-Truncated Data

	Fits Cox regression based on retrospectively ascertained times-to-event. The method uses Inverse-Probability-Weighting estimating equations. 
	"""
	
	homepage = "https://github.com/Bella2001/coxrt"
	cran = "coxrt" 

	version("1.0.3", md5="71bd86e08d9cc9ca2644ba9c2020ce9e")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-bb", type=("build", "run"))
	depends_on("r-inline", type=("build", "run"))
	depends_on("r-gss", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
