# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHistogramtools(RPackage):
	"""Utility Functions for R Histograms

	Provides a number of utility functions useful for manipulating large histograms.  This includes methods to trim, subset, merge buckets, merge histograms, convert to CDF, and calculate information loss due to binning.  It also provides a protocol buffer representations of the default R histogram class to allow histograms over large data sets to be computed and manipulated in a MapReduce environment.
	"""
	
	homepage = "https://r-forge.r-project.org/projects/histogramtools/"
	cran = "HistogramTools" 

	version("0.3.2", md5="4085c32ffd557f5db134e6b421ee40d5")

	depends_on("r-hmisc", type=("build", "run"))
	depends_on("r-ash", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
