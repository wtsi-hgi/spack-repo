# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLay(RPackage):
	"""Simple but Efficient Rowwise Jobs

	Creating efficiently new column(s) in a data frame (including tibble) by applying a function one row at a time.
	"""
	
	homepage = "https://courtiol.github.io/lay/"
	cran = "lay" 

	version("0.1.3", md5="d68a5ca36e82f350dabaf2b41317147c")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-vctrs", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
