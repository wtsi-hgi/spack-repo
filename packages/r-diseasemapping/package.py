# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDiseasemapping(RPackage):
	"""Modelling Spatial Variation in Disease Risk for Areal Data

	Formatting of population and case data, calculation of Standardized
    Incidence Ratios, and fitting the BYM model using 'INLA'. For details see Brown (2015) <doi:10.18637/jss.v063.i12>. 
	"""
	
	cran = "diseasemapping" 

	version("2.0.6", md5="2e9318a938858be8a84268c1a2d9c625")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-terra", type=("build", "run"))
