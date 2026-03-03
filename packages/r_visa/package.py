# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVisa(RPackage):
	"""Vegetation Imaging Spectroscopy Analyzer

	Provides easy-to-use tools for data analysis and visualization for hyperspectral remote sensing (also known as imaging spectroscopy), with 
    a particular focus on vegetation hyperspectral data analysis. It consists of a set of functions, ranging from the organization of hyperspectral data 
    in the proper data structure for spectral feature selection, calculation of vegetation index, multivariate analysis, as well as to the visualization 
    of spectra and results of analysis in the 'ggplot2' style.
	"""
	
	homepage = "https://github.com/kang-yu/visa"
	cran = "visa" 

	version("0.1.0", md5="ea5e175658a29dcf3eb52c97c22cbdab")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggpmisc", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
