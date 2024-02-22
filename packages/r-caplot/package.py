# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCaplot(RPackage):
	"""Correspondence Analysis with Geometric Frequency Interpretation

	Performs Correspondence Analysis on the given dataframe and plots the results in a scatterplot that emphasizes the geometric interpretation aspect of the analysis, following Borg-Groenen (2005) and Yelland (2010). It is particularly useful for highlighting the relationships between a selected row (or column) category and the column (or row) categories. See Borg-Groenen (2005, ISBN:978-0-387-28981-6); Yelland (2010) <doi:10.3888/tmj.12-4>.
	"""
	
	cran = "caplot" 

	version("0.2", md5="afbd96ea7d407004e22620724e58dcac")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-ca@0.71:", type=("build", "run"))
	depends_on("r-ggplot2@3.4:", type=("build", "run"))
	depends_on("r-ggrepel@0.9:", type=("build", "run"))
