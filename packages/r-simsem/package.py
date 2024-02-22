# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSimsem(RPackage):
	"""SIMulated Structural Equation Modeling

	Provides an easy framework for Monte Carlo simulation in structural equation modeling, which can be used for various purposes, such as such as model fit evaluation, power analysis, or missing data handling and planning. 
	"""
	
	homepage = "https://simsem.org/"
	cran = "simsem" 

	version("0.5-16", md5="e0b9f9ee918ffa3cebbc5b1148d05bc3")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-lavaan@0.6.7:", type=("build", "run"))
