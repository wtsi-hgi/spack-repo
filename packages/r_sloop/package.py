# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSloop(RPackage):
	"""Helpers for 'OOP' in R

	A collection of helper functions designed to help
    you to better understand object oriented programming in R,
    particularly using 'S3'.
	"""
	
	homepage = "https://github.com/r-lib/sloop"
	cran = "sloop" 

	version("1.0.1", md5="9e9142ac4e289090aa058df0c779891d")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-codetools", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tibble@2.0.1:", type=("build", "run"))
