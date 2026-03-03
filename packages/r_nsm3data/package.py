# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNsm3data(RPackage):
	"""Datasets to Accompany Hollander, Wolfe, and Chicken NSM3

	Designed to add datasets which are used in the Nonparametric Statistical Methods textbook, 3rd edition.
	"""
	
	cran = "nsm3data" 

	version("0.1", md5="ab842d3f9c4b918c6eb44c0b6958e404")

	depends_on("r@3.5:", type=("build", "run"))
