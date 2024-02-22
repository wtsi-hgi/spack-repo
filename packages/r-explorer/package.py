# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RExplorer(RPackage):
	"""Tools for Quickly Exploring Data

	Simplifies some complicated and labor intensive processes involved in exploring and explaining data.  Allows you to quickly and efficiently visualize the interaction between variables and simplifies the process of discovering covariation in your data.  Also includes some convenience features designed to remove as much redundant typing as possible.
	"""
	
	cran = "exploreR" 

	version("0.1", md5="4eb88043294bb736f026396fa42033de")

	depends_on("r@3.2.3:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
