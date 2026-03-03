# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLcmsqa(RPackage):
	"""Liquid Chromatography/Mass Spectrometry (LC/MS) Quality
Assessment

	The goal of 'LCMSQA' is to make it easy to check the quality of
             liquid chromatograph/mass spectrometry (LC/MS) experiments using a
             'shiny' application. This package provides interactive data
             visualizations for quality control (QC) samples, including total
             ion current chromatogram (TIC), base peak chromatogram (BPC), mass
             spectrum, extracted ion chromatogram (XIC), and feature detection
             results from internal standards or known metabolites.
	"""
	
	cran = "LCMSQA" 

	version("1.0.2", md5="1fdc568a76d0ec5268e6fd791b71fd66")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-bsplus", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-shinycssloaders", type=("build", "run"))
	depends_on("r-shinyjs", type=("build", "run"))
	depends_on("r-shinywidgets", type=("build", "run"))
