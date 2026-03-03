# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGamlssTr(RPackage):
	"""Generating and Fitting Truncated `gamlss.family' Distributions

	This is an add on package to GAMLSS. The purpose of this
        package is to allow users to defined truncated distributions in
        GAMLSS models. The main function gen.trun() generates truncated
        version of an existing GAMLSS family distribution.
	"""
	
	homepage = "https://www.gamlss.com/"
	cran = "gamlss.tr" 

	version("5.1-9", md5="8512f8702ac6cc6e7e19b65aa5d632d9")

	depends_on("r@2.2.1:", type=("build", "run"))
	depends_on("r-gamlss-dist", type=("build", "run"))
	depends_on("r-gamlss@5.0.0:", type=("build", "run"))
