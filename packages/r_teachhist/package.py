# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTeachhist(RPackage):
	"""A Collection of Amended Histograms Designed for Teaching
Statistics

	Statistics students often have problems understanding 
    the relation between a random variable's true scale and its z-values. 
    To allow instructors to better better visualize histograms for these 
    students, the package provides histograms with two horizontal 
    axis containing z-values and the true scale of the variable. 
    The function TeachHistDens() provides a density histogram with two axis.  
    TeachHistCounts() and TeachHistRelFreq() are variations for count and 
    relative frequency histograms, respectively. TeachConfInterv() and 
    TeachHypTest() help instructors to visualize confidence levels 
    and the results of hypothesis tests.
	"""
	
	cran = "TeachHist" 

	version("0.2.1", md5="fdc3bf1c922826c9bcf298928367c334")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
