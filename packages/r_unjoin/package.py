# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RUnjoin(RPackage):
	"""Separate a Data Frame by Normalization

	Separate a data frame in two based on key columns. The function
 unjoin() provides an inside-out version of a nested data frame. This is used
 to identify duplication and normalize it (in the database sense) by linking
 two tables with the redundancy removed. This is a basic requirement for
 detecting topology within spatial structures that has motivated the need for
 this package as a building block for workflows within more applied projects.
	"""
	
	homepage = "https://github.com/hypertidy/unjoin"
	cran = "unjoin" 

	version("0.1.0", md5="af3b257d476ce8cf7176a63b50077c7c")

	depends_on("r@3.3.2:", type=("build", "run"))
	depends_on("r-dplyr@0.5:", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
