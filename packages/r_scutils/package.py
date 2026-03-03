# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RScutils(RPackage):
	"""Utility Functions for Single-Cell RNA Sequencing Data

	Analysis of single-cell RNA sequencing data can be simple and
    clear with the right utility functions. This package collects such functions,
    aiming to fulfill the following criteria:
    code clarity over performance (i.e. plain R code instead of C code),
    most important analysis steps over completeness
    (analysis 'by hand', not automated integration etc.),
    emphasis on quantitative visualization (intensity-coded color scale, etc.).
	"""
	
	cran = "scUtils" 

	version("0.1.0", md5="5a6a8176bda1705481852b5fa6254261")

	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-viridis", type=("build", "run"))
	depends_on("r-viridislite", type=("build", "run"))
