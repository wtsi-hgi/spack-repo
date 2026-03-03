# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSos(RPackage):
	"""Search Contributed R Packages, Sort by Package

	Search contributed R packages, sort by package.
	"""
	
	cran = "sos" 

	version("2.1-7", md5="8b33e16060d01aa27b6c24c769dbbfee")

	depends_on("r-brew", type=("build", "run"))
