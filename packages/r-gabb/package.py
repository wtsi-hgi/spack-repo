# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGabb(RPackage):
	"""Facilitation of Data Preparation and Plotting Procedures for RDA
and PCA Analyses

	Help to the occasional R user for synthesis and enhanced graphical visualization of redundancy analysis (RDA) and principal component analysis (PCA) methods and objects.
  Inputs are : data frame, RDA (package 'vegan') and PCA (package 'FactoMineR') objects.
  Outputs are : synthesized results of RDA, displayed in console and saved in tables ; displayed and saved objects of PCA graphic visualization of individuals and variables projections with multiple graphic parameters.
	"""
	
	cran = "GABB" 

	version("0.3.8", md5="b162f54d36efc78fffd4e1c8f2c141dc")

	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-egg@0.4.5:", type=("build", "run"))
	depends_on("r-ggforce", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("r-ggplotify", type=("build", "run"))
	depends_on("r-ggpubr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-hotelling", type=("build", "run"))
	depends_on("r-pheatmap", type=("build", "run"))
	depends_on("r-vegan", type=("build", "run"))
