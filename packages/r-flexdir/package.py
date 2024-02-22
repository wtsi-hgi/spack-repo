# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFlexdir(RPackage):
	"""Tools to Work with the Flexible Dirichlet Distribution

	Provides tools to work with the Flexible Dirichlet
    distribution. The main features are an E-M algorithm for computing the maximum
    likelihood estimate of the parameter vector and a function based on conditional
    bootstrap to estimate its asymptotic variance-covariance matrix. It contains
    also functions to plot graphs, to generate random observations and to handle
    compositional data.
	"""
	
	cran = "FlexDir" 

	version("1.0", md5="e2573d3138d4f0afa2951943fc7c19c4")

	depends_on("r@3:", type=("build", "run"))
