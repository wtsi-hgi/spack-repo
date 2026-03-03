# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCengam(RPackage):
	"""Censored Regression with Smooth Terms

	Implementation of Tobit type I and type II families for censored regression using the 'mgcv' package, based on methods detailed in Woods (2016) <doi:10.1080/01621459.2016.1180986>.
	"""
	
	cran = "cenGAM" 

	version("0.5.3", md5="c45c13136acaefc2805221a3edf84a6f")

	depends_on("r@3.2.5:", type=("build", "run"))
	depends_on("r-mgcv@1.8.19:", type=("build", "run"))
