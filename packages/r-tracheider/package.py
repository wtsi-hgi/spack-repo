# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTracheider(RPackage):
	"""Standardize Tracheidograms

	Contains functions to standardize tracheid profiles
    using the traditional method (Vaganov) and a new method to standardize
    tracheidograms based on the relative position of tracheids within tree rings.
	"""
	
	cran = "tracheideR" 

	version("0.1.1", md5="fc3ca433009dc10ca0386c216fcdb770")

	depends_on("r@3.1.1:", type=("build", "run"))
	depends_on("r-tgram@0.2.2:", type=("build", "run"))
