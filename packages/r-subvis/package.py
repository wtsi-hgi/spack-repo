# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSubvis(RPackage):
	"""Visual Exploration of Protein Alignments Resulting from Multiple
Substitution Matrices

	Substitution matrices are important parameters in protein alignment algorithms. These matrices represent the likelihood that an amino acid will be substituted for another during mutation. This tool allows users to apply predefined and custom matrices and then explore the resulting alignments with interactive visualizations.  'SubVis' requires the availability of a web browser.
	"""
	
	cran = "SubVis" 

	version("2.0.2", md5="25874eaef7feaa200598250f2b065f4d")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
