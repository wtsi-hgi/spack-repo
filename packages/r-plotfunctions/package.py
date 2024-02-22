# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPlotfunctions(RPackage):
	"""Various Functions to Facilitate Visualization of Data and
Analysis

	When analyzing data, plots are a helpful tool for visualizing data and interpreting statistical models. This package provides a set of simple tools for building plots incrementally, starting with an empty plot region, and adding bars, data points, regression lines, error bars, gradient legends, density distributions in the margins, and even pictures. The package builds further on R graphics by simply combining functions and settings in order to reduce the amount of code to produce for the user. As a result, the package does not use formula input or special syntax, but can be used in combination with default R plot functions. Note: Most of the functions were part of the package 'itsadug', which is now split in two packages: 1. the package 'itsadug', which contains the core functions for visualizing and evaluating nonlinear regression models, and 2. the package 'plotfunctions', which contains more general plot functions.
	"""
	
	homepage = "https://jacolienvanrij.com/tutorials.html"
	cran = "plotfunctions" 

	version("1.4", md5="a9a017f69c002437b514e9aa779856db")

	depends_on("r@2.10:", type=("build", "run"))
