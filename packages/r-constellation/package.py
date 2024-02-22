# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RConstellation(RPackage):
	"""Identify Event Sequences Using Time Series Joins

	Examine any number of time series data frames to identify 
    instances in which various criteria are met within specified time
    frames. In clinical medicine, these types of events are often
    called "constellations of signs and symptoms", because a single 
    condition depends on a series of events occurring within a certain 
    amount of time of each other. This package was written to work with
    any number of time series data frames and is optimized for speed 
    to work well with data frames with millions of rows.
	"""
	
	homepage = "https://github.com/marksendak/constellation"
	cran = "constellation" 

	version("0.2.0", md5="8ffd514d5bfba230bbdabc6e551cdf97")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-data-table@1.9.5:", type=("build", "run"))
