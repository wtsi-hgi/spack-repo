# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RShinymolbio(RPackage):
	"""Molecular Biology Visualization Tools for 'Shiny' Apps

	Interactive visualization of 'RDML' files via 'shiny' apps. 
  Package provides (1) PCR plate interface with ability to select
  individual tubes and (2) amplification/melting plots with fast hiding and 
  highlighting individual curves.
	"""
	
	homepage = "https://github.com/kablag/shinyMolBio"
	cran = "shinyMolBio" 

	version("0.2", md5="1a7092b5a33fdfe7c4a0165087c5ede7")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-rdml", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-whisker", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
