# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RZipfr(RPackage):
	"""Statistical Models for Word Frequency Distributions

	Statistical models and utilities for the analysis of word frequency distributions.
	The utilities include functions for loading, manipulating and visualizing word frequency
	data and vocabulary growth curves.  The package also implements several statistical 
	models for the distribution of word frequencies in a population.  (The name of this package 
	derives from the most famous word frequency distribution, Zipf's law.)
	"""
	
	homepage = "https://zipfR.R-Forge.R-project.org/"
	cran = "zipfR" 

	version("0.6-70", md5="deeae902bfac2c26adc385a5da81cb4a")

	depends_on("r@3:", type=("build", "run"))
