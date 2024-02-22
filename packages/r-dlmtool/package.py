# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDlmtool(RPackage):
	"""Data-Limited Methods Toolkit

	A collection of data-limited management procedures that can be evaluated 
    with management strategy evaluation with the 'MSEtool' package, or applied to 
    fishery data to provide management recommendations.
	"""
	
	cran = "DLMtool" 

	version("6.0.6", md5="07e37ca11dc3b91ed80f1471b165750e")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-msetool", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-tmb", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
