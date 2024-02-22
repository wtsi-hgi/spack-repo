# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPrqlr(RPackage):
	"""R Bindings for the 'prqlc' Rust Library

	
    Provides a function to convert 'PRQL' strings to 'SQL' strings.
    Combined with other R functions that take 'SQL' as an argument,
    'PRQL' can be used on R.
	"""
	
	homepage = "https://prql.github.io/prqlc-r/"
	cran = "prqlr" 

	version("0.8.0", md5="a5f867fdf74b67f50ec170f789d84674")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("rust", type=("build", "link", "run"))
