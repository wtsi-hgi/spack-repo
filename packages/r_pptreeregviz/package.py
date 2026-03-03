# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPptreeregviz(RPackage):
	"""Projection Pursuit Regression Tree Visualization

	It was developed as a tool for exploring 'PPTreereg' (Projection Pursuit TREE of REGression). 
  It uses various projection pursuit indexes and 'XAI' (eXplainable Artificial Intelligence) methods to help 
  understand the model by finding connections between the input variables and prediction values of the model. 
  The 'KernelSHAP' (Aas, Jullum and Løland (2019) <arXiv:1903.10464>) algorithm was modified to fit ‘PPTreereg’, 
  and some codes were modified from the 'shapr' package (Sellereite, Nikolai, and Martin Jullum (2020) <doi:10.21105/joss.02027>). 
  The implemented methods help to explore the model at the single instance level as well as at the whole dataset level. 
  Users can compare with other machine learning models by applying it to the 'DALEX' package of 'R'.
	"""
	
	homepage = "https://github.com/sunsmiling/PPtreeregViz"
	cran = "PPtreeregViz" 

	version("2.0.5", md5="3246a15d4ee8c0850ce40285a2c8eaa6")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-dalex", type=("build", "run"))
	depends_on("r-shapr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-pptreeviz", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
