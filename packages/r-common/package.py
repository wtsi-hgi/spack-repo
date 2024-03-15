# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCommon(RPackage):
	"""Solutions for Common Problems in Base R

	Contains functions for solving commonly encountered problems while
    programming in R. This package is intended to provide a lightweight 
    supplement to Base R, and will be useful for almost any R user.
	"""
	
	homepage = "https://common.r-sassy.org"
	cran = "common" 

	version("1.1.2", md5="c5850761d729ffb92977f0ecb0b8e84f")

	depends_on("r@3.6:", type=("build", "run"))
