# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLabdsv(RPackage):
	"""Ordination and Multivariate Analysis for Ecology

	A variety of ordination and community analyses
   useful in analysis of data sets in community ecology.  
   Includes many of the common ordination methods, with 
   graphical routines to facilitate their interpretation, 
   as well as several novel analyses.
	"""
	
	cran = "labdsv" 

	version("2.1-0", md5="59d0f730adccd6abb1655a510a1985ed")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-rtsne", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
