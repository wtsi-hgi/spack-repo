# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWbs(RPackage):
	"""Wild Binary Segmentation for Multiple Change-Point Detection

	Provides efficient implementation of the Wild Binary Segmentation and Binary
    Segmentation algorithms for estimation of the number and locations of
    multiple change-points in the piecewise constant function plus Gaussian
    noise model.
	"""
	
	cran = "wbs" 

	version("1.4", md5="2f4daaa84290d4e81002b251f15d8a56")

