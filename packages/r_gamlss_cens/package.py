# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGamlssCens(RPackage):
	"""Fitting an Interval Response Variable Using `gamlss.family'
Distributions

	This is an add-on package to GAMLSS. The purpose of this
        package is to allow users to fit interval response variables in
        GAMLSS models. The main function gen.cens() generates a
        censored version of an existing GAMLSS family distribution.
	"""
	
	homepage = "https://www.gamlss.com/"
	cran = "gamlss.cens" 

	version("5.0-7", md5="b847a16e497afd9aad28b2cbfd37c29d")

	depends_on("r@2.2.1:", type=("build", "run"))
	depends_on("r-gamlss-dist", type=("build", "run"))
	depends_on("r-gamlss", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
