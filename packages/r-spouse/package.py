# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpouse(RPackage):
	"""Scatter Plots Over-Viewed Using Summary Ellipses

	Summary ellipses superimposed on a scatter plot contain all bi-variate summary
            statistics for regression analysis. Furthermore, the outer ellipse flags potential
            outliers. Multiple groups can be compared in terms of centers and spreads as illustrated
            in the examples.
	"""
	
	cran = "SPOUSE" 

	version("0.1.0", md5="a97b6de1bda3887e581211d2e52d3236")

