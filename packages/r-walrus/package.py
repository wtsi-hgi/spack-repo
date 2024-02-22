# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWalrus(RPackage):
	"""Robust Statistical Methods

	A toolbox of common robust statistical tests, including robust
  descriptives, robust t-tests, and robust ANOVA. It is also available as a
  module for 'jamovi' (see <https://www.jamovi.org> for more information).
  Walrus is based on the WRS2 package by Patrick Mair, which is in turn based on
  the scripts and work of Rand Wilcox. These analyses are described in depth in
  the book 'Introduction to Robust Estimation & Hypothesis Testing'.
	"""
	
	homepage = "https://github.com/jamovi/walrus"
	cran = "walrus" 

	version("1.0.5", md5="f0b7a80091053cfd956bb5bff1286ebd")

	depends_on("r-wrs2", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-jmvcore@2.2:", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
