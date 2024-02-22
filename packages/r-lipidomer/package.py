# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLipidomer(RPackage):
	"""Integrative Visualizations of the Lipidome

	Create lipidome-wide heatmaps of statistics with the 'lipidomeR'.
    The 'lipidomeR' provides a streamlined pipeline for the systematic 
    interpretation of the lipidome through publication-ready visualizations 
    of regression models fitted on lipidomics data. 
    With 'lipidomeR', associations between covariates and the lipidome 
    can be interpreted systematically and intuitively through heatmaps, where 
    lipids are categorized by the lipid class and are presented on 
    two-dimensional maps organized by the lipid size and level of saturation. 
    This way, the 'lipidomeR' helps you gain an immediate understanding of 
    the multivariate patterns in the lipidome already at first glance.
    You can create lipidome-wide heatmaps of statistical associations, changes, 
    differences, variation, or other lipid-specific values.  
    The heatmaps are provided with publication-ready quality and the results 
    behind the visualizations are based on rigorous statistical models.
	"""
	
	homepage = "https://tommi-s.github.io/"
	cran = "lipidomeR" 

	version("0.1.2", md5="d271fb42eba9c929d351cd8a2550be6b")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-biocmanager", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-shadowtext", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tableone", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
