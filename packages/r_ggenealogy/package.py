# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGgenealogy(RPackage):
	"""Visualization Tools for Genealogical Data

	Methods for searching through genealogical data and displaying the results. Plotting algorithms assist with data exploration and publication-quality image generation. Includes interactive genealogy visualization tools. Provides parsing and calculation methods for variables in descendant branches of interest. Uses the Grammar of Graphics.
	"""
	
	cran = "ggenealogy" 

	version("1.0.3", md5="a2a4174d822e769f0b500b1dca53db79")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-ggplot2@2.2:", type=("build", "run"))
	depends_on("r-igraph@0.7.1:", type=("build", "run"))
	depends_on("r-plyr@1.8.1:", type=("build", "run"))
	depends_on("r-reshape2@1.4:", type=("build", "run"))
	depends_on("r-plotly@4.5.6:", type=("build", "run"))
