# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAgridat(RPackage):
	"""Agricultural Datasets

	Datasets from books, papers, and websites related to agriculture.
    Example graphics and analyses are included. Data come from small-plot trials,
    multi-environment trials, uniformity trials, yield monitors, and more.
	"""
	
	homepage = "https://kwstat.github.io/agridat/"
	cran = "agridat" 

	version("1.23", md5="ecc5d3574494bd1cdc1236f70fcec023")

