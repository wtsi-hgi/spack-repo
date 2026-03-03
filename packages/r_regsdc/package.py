# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRegsdc(RPackage):
	"""Information Preserving Regression-Based Tools for Statistical
Disclosure Control

	Implementation of the methods described in the paper with the above title: Langsrud, Ø. (2019) <doi:10.1007/s11222-018-9848-9>. The package can be used to generate synthetic or hybrid continuous microdata, and the relationship to the original data can be controlled in several ways. A function for replacing suppressed tabular cell frequencies with decimal numbers is included.
	"""
	
	homepage = "https://github.com/olangsrud/RegSDC"
	cran = "RegSDC" 

	version("0.7.0", md5="45067cb6f30496bd851e0538781d129e")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-ssbtools@1.3.4:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
