# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFbasics(RPackage):
	"""Rmetrics - Markets and Basic Statistics

	Provides a collection of functions to 
    explore and to investigate basic properties of financial returns 
    and related quantities.
    The covered fields include techniques of explorative data analysis
    and the investigation of distributional properties, including
    parameter estimation and hypothesis testing. Even more there are
    several utility functions for data handling and management.
	"""
	
	homepage = "https://geobosh.github.io/fBasicsDoc/"
	cran = "fBasics" 

	version("4032.96", md5="25280afb23459d18ed197a70be669efe")

	depends_on("r@2.15.1:", type=("build", "run"))
	depends_on("r-timedate", type=("build", "run"))
	depends_on("r-timeseries@4021.105:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-spatial", type=("build", "run"))
	depends_on("r-gss", type=("build", "run"))
	depends_on("r-stabledist", type=("build", "run"))
