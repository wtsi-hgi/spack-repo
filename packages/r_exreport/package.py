# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RExreport(RPackage):
	"""Fast, Reliable and Elegant Reproducible Research

	Analysis of experimental results and automatic report generation in both interactive HTML and LaTeX. This package ships with a rich interface for data modeling and built in functions for the rapid application of statistical tests and generation of common plots and tables with publish-ready quality.
	"""
	
	cran = "exreport" 

	version("0.4.1", md5="c65362b4b939d9424de796696fe1a5a3")

	depends_on("r@3.1.1:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
