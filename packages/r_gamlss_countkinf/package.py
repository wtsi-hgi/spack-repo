# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGamlssCountkinf(RPackage):
	"""Generating and Fitting K-Inflated 'discrete gamlss.family'
Distributions

	This is an add on package to 'GAMLSS'. The main purpose of this package is generating and fitting inflated distributions at any desired point (0, 1, 2, ...). The function gen.Kinf() generates K-inflated version of an existing discrete 'GAMLSS' family distribution.
	"""
	
	homepage = "http://www.gamlss.org/"
	cran = "gamlss.countKinf" 

	version("3.5.1", md5="290c92a20f246821b9f062067a2084d4")

	depends_on("r@2.2.1:", type=("build", "run"))
	depends_on("r-gamlss-dist", type=("build", "run"))
	depends_on("r-gamlss@5.0.0:", type=("build", "run"))
