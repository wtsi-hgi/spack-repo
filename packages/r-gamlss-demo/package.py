# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGamlssDemo(RPackage):
	"""Demos for GAMLSS

	Demos for smoothing and gamlss.family distributions.
	"""
	
	homepage = "http://www.gamlss.org/"
	cran = "gamlss.demo" 

	version("4.3-3", md5="5639158da3e881e1dcbfe696e4666c1c")

	depends_on("r@2.4:", type=("build", "run"))
	depends_on("r-rpanel@1.1.1:", type=("build", "run"))
	depends_on("r-gamlss-dist", type=("build", "run"))
	depends_on("r-gamlss-tr", type=("build", "run"))
