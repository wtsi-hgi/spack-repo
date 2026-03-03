# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RClassifierplots(RPackage):
	"""Generates a Visualization of Classifier Performance as a Grid of
Diagnostic Plots

	
  Generates a visualization of binary classifier performance as a grid of
  diagnostic plots with just one function call. Includes ROC curves,
  prediction density, accuracy, precision, recall and calibration plots, all using
  ggplot2 for easy modification.
  Debug your binary classifiers faster and easier!
	"""
	
	homepage = "https://github.com/adefazio/classifierplots"
	cran = "classifierplots" 

	version("1.4.0", md5="c21a1f5f7fe5c0dfc29e75ba22988094")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-ggplot2@2.2:", type=("build", "run"))
	depends_on("r-data-table@1.10:", type=("build", "run"))
	depends_on("r-rcpp@0.12:", type=("build", "run"))
	depends_on("r-rocr", type=("build", "run"))
	depends_on("r-caret", type=("build", "run"))
	depends_on("r-gridextra@2.2:", type=("build", "run"))
	depends_on("r-png", type=("build", "run"))
