# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCoxmos(RPackage):
	"""Cox MultiBlock Survival

	This software package provides Cox survival analysis for high-dimensional and multiblock datasets. 
             It encompasses a suite of functions dedicated from the classical Cox regression to newest analysis,
             including Cox proportional hazards model, Stepwise Cox regression, and Elastic-Net Cox regression, 
             Sparse Partial Least Squares Cox regression (sPLS-COX) incorporating three distinct strategies, 
             and two Multiblock-PLS Cox regression (MB-sPLS-COX) methods. This tool is designed to adeptly handle 
             high-dimensional data, and provides tools for cross-validation, plot generation, and additional resources 
             for interpreting results. While references are available within the corresponding functions, 
             key literature is mentioned below.
             Terry M Therneau (2024) <https://CRAN.R-project.org/package=survival>,
             Noah Simon et al. (2011) <doi:10.18637/jss.v039.i05>,
             Philippe Bastien et al. (2005) <doi:10.1016/j.csda.2004.02.005>,
             Philippe Bastien (2008) <doi:10.1016/j.chemolab.2007.09.009>,
             Philippe Bastien et al. (2014) <doi:10.1093/bioinformatics/btu660>,
             Kassu Mehari Beyene and Anouar El Ghouch (2020) <doi:10.1002/sim.8671>,
             Florian Rohart et al. (2017) <doi:10.1371/journal.pcbi.1005752>.
	"""
	
	homepage = "https://github.com/BiostatOmics/Coxmos"
	cran = "Coxmos" 

	version("1.0.0", md5="4443f512b6feceef453600729ea711f9")
	version("1.0.2", md5="ea49c17293e462fcbebfbe59109e4199")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-caret", type=("build", "run"))
	depends_on("r-cowplot", type=("build", "run"))
	depends_on("r-furrr", type=("build", "run"))
	depends_on("r-future", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggpubr", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-mixomics", type=("build", "run"))
	depends_on("r-progress", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
	depends_on("r-scattermore", type=("build", "run"))
	depends_on("r-survcomp", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-survminer", type=("build", "run"))
	depends_on("r-svglite", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
