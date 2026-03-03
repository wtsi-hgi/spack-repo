# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWgaim(RPackage):
	"""Whole Genome Average Interval Mapping for QTL Detection and
Estimation using ASReml-R

	A computationally efficient whole genome approach to detecting and estimating significant QTL in linkage maps using the flexible linear mixed modelling functionality of ASReml-R.
	"""
	
	cran = "wgaim" 

	version("2.0-1", md5="efc991e621183e9ee31735965d4241ff")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-qtl", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
