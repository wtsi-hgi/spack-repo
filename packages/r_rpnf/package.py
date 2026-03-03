# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRpnf(RPackage):
	"""Point and Figure Package

	A set of functions to analyze and print the development of a
    commodity using the Point and Figure (P&F) approach. A P&F processor can be used
    to calculate daily statistics for the time series. These statistics can be used
    for deeper investigations as well as to create plots. Plots can be generated as
    well known X/O Plots in plain text format, and additionally in a more graphical
    format.
	"""
	
	cran = "rpnf" 

	version("1.0.5", md5="b48a279a5acf8fd5f0abb7d054176574")

	depends_on("r@3:", type=("build", "run"))
