# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAuditor(RPackage):
	"""Model Audit - Verification, Validation, and Error Analysis

	Provides an easy to use unified interface for creating validation plots for any model. 
  The 'auditor' helps to avoid repetitive work consisting of writing code needed to create residual plots. 
  This visualizations allow to asses and compare the goodness of fit, performance, and similarity of models. 
	"""
	
	homepage = "https://github.com/ModelOriented/auditor"
	cran = "auditor" 

	version("1.3.5", md5="a3180ed26a6e101e679cc9bfb83b3c3c")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dalex", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-hnp", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
