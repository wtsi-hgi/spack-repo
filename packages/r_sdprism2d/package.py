# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSdprism2d(RPackage):
	"""Visualizing the Standard Deviation as the Size of a Prism

	We visualize the standard deviation of a data set as the size of a prism whose volume equals the total volume of several prisms made from the Empirical Cumulative Distribution Function.
	"""
	
	cran = "SDPrism2D" 

	version("0.1.1", md5="31f7b9b955aa79dcdf03c491b089a066")

