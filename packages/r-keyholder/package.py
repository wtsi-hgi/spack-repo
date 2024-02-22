# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKeyholder(RPackage):
	"""Store Data About Rows

	Tools for keeping track of information, named
    "keys", about rows of data frame like objects. This is done by
    creating special attribute "keys" which is updated after every change
    in rows (subsetting, ordering, etc.).  This package is designed to
    work tightly with 'dplyr' package.
	"""
	
	homepage = "https://echasnovski.github.io/keyholder/"
	cran = "keyholder" 

	version("0.1.7", md5="597c9cbeda141f59f9aa3f0de3684526")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-dplyr@0.7:", type=("build", "run"))
	depends_on("r-rlang@0.1:", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
