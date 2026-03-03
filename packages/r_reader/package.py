# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RReader(RPackage):
	"""Suite of Functions to Flexibly Read Data from Files

	A set of functions to simplify reading data from files. The main function, reader(), should read most common R datafile types without needing any parameters except the filename. Other functions provide simple ways of handling file paths and extensions, and automatically detecting file format and structure.
	"""
	
	cran = "reader" 

	version("1.0.6", md5="8d43cf91c81d10f690048b00a7f8c774")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-ncmisc@1.1:", type=("build", "run"))
