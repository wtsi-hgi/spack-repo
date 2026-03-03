# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROrdinalgmifs(RPackage):
	"""Ordinal Regression for High-Dimensional Data

	Provides a function for fitting cumulative link, adjacent category, forward and backward continuation ratio, and stereotype ordinal response models when the number of parameters exceeds the sample size, using the the generalized monotone incremental forward stagewise method.
	"""
	
	cran = "ordinalgmifs" 

	version("1.0.8", md5="645b297015368a222ef0f05279dedce7")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
