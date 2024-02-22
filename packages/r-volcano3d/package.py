# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVolcano3d(RPackage):
	"""3D Volcano Plots and Polar Plots for Three-Class Data

	Generates interactive plots for analysing and visualising 
    three-class high dimensional data. It is particularly suited to visualising 
    differences in continuous attributes such as gene/protein/biomarker 
    expression levels between three groups. Differential gene/biomarker 
    expression analysis between two classes is typically shown as a volcano 
    plot. However, with three groups this type of visualisation is particularly 
    difficult to interpret. This package generates 3D volcano plots and 3-way 
    polar plots for easier interpretation of three-class data.
	"""
	
	homepage = "https://katrionagoldmann.github.io/volcano3D/index.html"
	cran = "volcano3D" 

	version("2.0.9", md5="a6ae457a6a9481ef758842e5e9d4374a")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggpubr", type=("build", "run"))
	depends_on("r-htmlwidgets", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-rfast", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-matrixtests", type=("build", "run"))
