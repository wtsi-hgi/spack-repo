# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RThief(RPackage):
	"""Temporal Hierarchical Forecasting

	Methods and tools for generating forecasts at different temporal
    frequencies using a hierarchical time series approach.
	"""
	
	homepage = "http://pkg.robjhyndman.com/thief"
	cran = "thief" 

	version("0.3", md5="175272d0c6fdce01e1a85079762a877d")

	depends_on("r@3.0.2:", type=("build", "run"))
	depends_on("r-forecast@7.2:", type=("build", "run"))
	depends_on("r-hts", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
