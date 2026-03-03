# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RProtviz(RPackage):
	"""Visualizing and Analyzing Mass Spectrometry Related Data in
Proteomics

	Helps with quality checks, visualizations 
    and analysis of mass spectrometry data, coming from proteomics 
    experiments. The package is developed, tested and used at the Functional 
    Genomics Center Zurich <https://fgcz.ch>. We use this package
    mainly for prototyping, teaching, and having fun with proteomics data.
    But it can also be used to do data analysis for small scale data sets.
	"""
	
	homepage = "https://github.com/cpanse/protViz/"
	cran = "protViz" 

	version("0.7.9", md5="64cb0eaece890227078d75c5b5b24498")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-rcpp@1:", type=("build", "run"))
