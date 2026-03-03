# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RProtein8k(RPackage):
	"""Perform Analysis and Create Visualizations of Proteins

	Read Protein Data Bank (PDB) files, performs its analysis, and 
    presents the result using different visualization types including 3D. The 
    package also has additional capability for handling Virus Report data from 
    the National Center for Biotechnology Information (NCBI) database.
    Nature Structural Biology 10, 980 (2003) <doi:10.1038/nsb1203-980>.
    US National Library of Medicine (2021) <https://www.ncbi.nlm.nih.gov/datasets/docs/reference-docs/data-reports/virus/>.
	"""
	
	cran = "protein8k" 

	version("0.0.1", md5="457a4c643ba1a92cf7cfa759a6eaace1")

	depends_on("r@3.1.2:", type=("build", "run"))
	depends_on("r-pryr", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-magick", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-rjson", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
