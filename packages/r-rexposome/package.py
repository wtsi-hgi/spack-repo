# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRexposome(RPackage):
	"""Exposome exploration and outcome data analysis

	Package that allows to explore the exposome and to perform association analyses between exposures and health outcomes.
	"""
	
	bioc = "rexposome"

	version("1.30.0", commit="7b965f856bd29e8252b7affc764b1552db0cc574")
	version("1.24.1", commit="05e3856399772662c8b2d60c50f3de17fea6ae27")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-lsr", type=("build", "run"))
	depends_on("r-factominer", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-circlize", type=("build", "run"))
	depends_on("r-corrplot", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggridges", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-pryr", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-imputelcmd", type=("build", "run"))
	depends_on("r-scatterplot3d", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-hmisc", type=("build", "run"))
	depends_on("r-gplots", type=("build", "run"))
	depends_on("r-gtools", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-lme4", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("r-mice", type=("build", "run"))
