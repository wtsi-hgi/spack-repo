# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMakemyprior(RPackage):
	"""Intuitive Construction of Joint Priors for Variance Parameters

	Tool for easy prior construction and visualization. It helps to formulates joint prior distributions for variance parameters in latent Gaussian models. The resulting prior is robust and can be created in an intuitive way. A graphical user interface (GUI) can be used to choose the joint prior, where the user can click through the model and select priors. An extensive guide is available in the GUI. The package allows for direct inference with the specified model and prior. Using a hierarchical variance decomposition, we formulate a joint variance prior that takes the whole model structure into account. In this way, existing knowledge can intuitively be incorporated at the level it applies to. Alternatively, one can use independent variance priors for each model components in the latent Gaussian model.
	"""
	
	cran = "makemyprior" 

	version("1.1.0", md5="f4c9e71ba5df9f4e5d44904c102ef14d")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-shinyjs", type=("build", "run"))
	depends_on("r-shinybs", type=("build", "run"))
	depends_on("r-visnetwork", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
