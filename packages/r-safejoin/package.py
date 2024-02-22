# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSafejoin(RPackage):
	"""Perform "Safe" Table Joins

	The goal of 'safejoin' is to guarantee that when performing joins extra rows are not added to your data. 'safejoin' provides a wrapper around 'dplyr::left_join' that will raise an error when extra rows are unexpectedly added to your data. This can be useful when working with data where you expect there to be a many to one relationship but you are not certain the relationship holds.
	"""
	
	homepage = "https://github.com/SamEdwardes/safejoin"
	cran = "safejoin" 

	version("0.1.0", md5="97e489b1de01f63db7204867c122f2bb")

	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
