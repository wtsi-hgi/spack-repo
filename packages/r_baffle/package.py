# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBaffle(RPackage):
	"""Make Waffle Plots with Base Graphics

	Waffle plots are rectangular pie charts that represent a quantity or abundances using
    colored squares or other symbol. This makes them better at transmitting information as the
    discrete number of squares is easier to read than the circular area of pie charts.
    While the original waffle charts were rectangular with 10 rows and columns, with a single square
    representing 1%, they are nowadays popular in various infographics to visualize any
    proportional ratios.
	"""
	
	homepage = "https://j-moravec.github.io/baffle/"
	cran = "baffle" 

	version("0.2.2", md5="cd9e9f6da5e2d1ed926a7905e821bb0a")

