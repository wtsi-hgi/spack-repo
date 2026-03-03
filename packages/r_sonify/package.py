# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSonify(RPackage):
	"""Data Sonification - Turning Data into Sound

	Sonification (or audification) is the process of representing data by sounds in the audible range. This package provides the R function sonify() that transforms univariate data, sampled at regular or irregular intervals, into a continuous sound with time-varying frequency. The ups and downs in frequency represent the ups and downs in the data. Sonify provides a substitute for R's plot function to simplify data analysis for the visually impaired.
	"""
	
	cran = "sonify" 

	version("0.0-1", md5="796634c3c0044e0fd200a341dd3b1e38")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-tuner@1.3.1:", type=("build", "run"))
