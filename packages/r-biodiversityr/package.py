# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBiodiversityr(RPackage):
	"""Package for Community Ecology and Suitability Analysis

	Graphical User Interface (via the R-Commander) and utility functions (often based on the vegan package) for statistical analysis of biodiversity and ecological communities, including species accumulation curves, diversity indices, Renyi profiles, GLMs for analysis of species abundance and presence-absence, distance matrices, Mantel tests, and cluster, constrained and unconstrained ordination analysis. A book on biodiversity and community ecology analysis is available for free download from the website. In 2012, methods for (ensemble) suitability modelling and mapping were expanded in the package.
	"""
	
	homepage = "http://www.worldagroforestry.org/output/tree-diversity-analysis"
	cran = "BiodiversityR" 

	version("2.15-4", md5="1178338fa462f2214242d1bdd37647f2")

	depends_on("r@3.2.2:", type=("build", "run"))
	depends_on("r-vegan@2.6.4:", type=("build", "run"))
	depends_on("r-rcmdr@2.9.1:", type=("build", "run"))
	depends_on("r-ggplot2@3.3.3:", type=("build", "run"))
