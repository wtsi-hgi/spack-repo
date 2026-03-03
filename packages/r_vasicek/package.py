# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVasicek(RPackage):
	"""Miscellaneous Functions for Vasicek Distribution

	Provide a collection of miscellaneous R functions
    related to the Vasicek distribution with the intent to make
    the lives of risk modelers easier.
	"""
	
	homepage = "https://github.com/statcompute/vasicek"
	cran = "vasicek" 

	version("0.0.3", md5="02d17e01573c2bb93f2dcfe69284b4a0")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
