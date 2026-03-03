# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RClda(RPackage):
	"""Convolution-Based Linear Discriminant Analysis

	Contains a time series classification method that obtains a set of filters that maximize the between-class and minimize the within-class distances.
	"""
	
	cran = "clda" 

	version("0.1", md5="b4ef8256923a30104a150cf53f371c09")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
