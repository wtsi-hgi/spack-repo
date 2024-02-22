# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPreputils(RPackage):
	"""Utilities for Preparation of Data Analysis

	Miscellaneous small utilities are provided to mitigate issues with messy, inconsistent or high dimensional data and help for preprocessing and preparing analyses.
	"""
	
	cran = "preputils" 

	version("1.0.3", md5="f72bf738e06d783beb94a3f330443da0")

	depends_on("r-data-table", type=("build", "run"))
