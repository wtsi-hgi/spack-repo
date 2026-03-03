# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAirgrteaching(RPackage):
	"""Teaching Hydrological Modelling with the GR Rainfall-Runoff
Models ('Shiny' Interface Included)

	Add-on package to the 'airGR' package that simplifies its use and is aimed at being used for teaching hydrology. The package provides 1) three functions that allow to complete very simply a hydrological modelling exercise 2) plotting functions to help students to explore observed data and to interpret the results of calibration and simulation of the GR ('Génie rural') models 3) a 'Shiny' graphical interface that allows for displaying the impact of model parameters on hydrographs and models internal variables.
	"""
	
	homepage = "https://hydrogr.github.io/airGRteaching/"
	cran = "airGRteaching" 

	version("0.3.2", md5="e5f899dc564fcf4396b5c69c6fa200c7")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-airgr@1.6.9.27:", type=("build", "run"))
	depends_on("r-dygraphs@1.1.1.6:", type=("build", "run"))
	depends_on("r-markdown", type=("build", "run"))
	depends_on("r-plotrix", type=("build", "run"))
	depends_on("r-shiny@1.1:", type=("build", "run"))
	depends_on("r-shinyjs@1:", type=("build", "run"))
	depends_on("r-xts", type=("build", "run"))
