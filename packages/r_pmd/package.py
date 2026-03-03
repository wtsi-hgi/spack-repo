# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPmd(RPackage):
	"""Paired Mass Distance Analysis for GC/LC-MS Based Non-Targeted
Analysis and Reactomics Analysis

	Paired mass distance (PMD) analysis proposed in Yu, Olkowicz and Pawliszyn (2018) <doi:10.1016/j.aca.2018.10.062> for gas/liquid chromatography–mass spectrometry (GC/LC-MS) based non-targeted analysis. PMD analysis including GlobalStd algorithm and structure/reaction directed analysis. GlobalStd algorithm could found independent peaks in m/z-retention time profiles based on retention time hierarchical cluster analysis and frequency analysis of paired mass distances within retention time groups. Structure directed analysis could be used to find potential relationship among those independent peaks in different retention time groups based on frequency of paired mass distances. Reactomics analysis could also be performed to build PMD network, assign sources and make biomarker reaction discovery. GUIs for PMD analysis is also included as 'shiny' applications.
	"""
	
	homepage = "https://yufree.github.io/pmd/"
	cran = "pmd" 

	version("0.2.1", md5="d0336226b54e6b638aaf3440c1226a1c")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-envigcms", type=("build", "run"))
