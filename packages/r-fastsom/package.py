# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFastsom(RPackage):
	"""Fast Calculation of Spillover Measures

	Functions for computing spillover measures, especially spillover
    tables and spillover indices, as well as their average, minimal, and maximal
    values.
	"""
	
	cran = "fastSOM" 

	version("1.0.1", md5="058f8bfebd8c7484a84169546356bf48")

