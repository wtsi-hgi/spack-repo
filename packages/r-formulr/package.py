# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFormulr(RPackage):
	"""Comprehensive Tools for Drug Formulation Analysis and
Visualization

	This presents a comprehensive set of tools for the analysis and visualization of drug formulation data. It includes functions for statistical analysis, regression modeling, hypothesis testing, and comparative analysis to assess the impact of formulation parameters on drug release and other critical attributes. Additionally, the package offers a variety of data visualization functions, such as scatterplots, histograms, and boxplots, to facilitate the interpretation of formulation data. With its focus on usability and efficiency, this package aims to streamline the drug formulation process and aid researchers in making informed decisions during formulation design and optimization.
	"""
	
	cran = "FormulR" 

	version("1.0.0", md5="0b4d755b7146a41163ed6b1906b2989a")

	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
