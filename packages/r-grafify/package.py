# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGrafify(RPackage):
	"""Easy Graphs for Data Visualisation and Linear Models for ANOVA

	Easily explore data by plotting graphs with a few lines of code. Use these ggplot() wrappers to quickly draw graphs of scatter/dots with box-whiskers, violins or SD error bars, data distributions, before-after graphs, factorial ANOVA and more. Customise graphs in many ways, for example, by choosing from colour blind-friendly palettes (12 discreet, 3 continuous and 2 divergent palettes). Use the simple code for ANOVA as ordinary (lm()) or mixed-effects linear models (lmer()), including randomised-block or repeated-measures designs, and fit non-linear outcomes as a generalised additive model (gam) using mgcv(). Obtain estimated marginal means and perform post-hoc comparisons on fitted models (via emmeans()). Also includes small datasets for practising code and teaching basics before users move on to more complex designs. See vignettes for details on usage <https://grafify-vignettes.netlify.app/>. Citation: <doi:10.5281/zenodo.5136508>.
	"""
	
	homepage = "https://github.com/ashenoy-cmbi/grafify"
	cran = "grafify" 

	version("4.0.1", md5="275ca922a5f0141c54974feae5fc1f42")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-ggplot2@3.4:", type=("build", "run"))
	depends_on("r-car", type=("build", "run"))
	depends_on("r-emmeans", type=("build", "run"))
	depends_on("r-hmisc", type=("build", "run"))
	depends_on("r-lme4", type=("build", "run"))
	depends_on("r-lmertest", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
	depends_on("r-patchwork", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
