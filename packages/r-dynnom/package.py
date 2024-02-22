# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDynnom(RPackage):
	"""Visualising Statistical Models using Dynamic Nomograms

	Demonstrate the results of a statistical model object as a dynamic nomogram in an RStudio panel or web browser. The package provides two generics functions: DynNom, which display statistical model objects as a dynamic nomogram; DNbuilder, which builds required scripts to publish a dynamic nomogram on a web server such as the <https://www.shinyapps.io/>. Current version of 'DynNom' supports stats::lm, stats::glm, survival::coxph, rms::ols, rms::Glm, rms::lrm, rms::cph, mgcv::gam and gam::gam model objects.
	"""
	
	cran = "DynNom" 

	version("5.0.2", md5="16bcbc2df50a460a0d108a82fb84c122")

	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-survival@2.38.3:", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-ggplot2@2.1:", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-stargazer", type=("build", "run"))
	depends_on("r-prediction", type=("build", "run"))
	depends_on("r-rms", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-compare", type=("build", "run"))
	depends_on("r-bbmisc", type=("build", "run"))
