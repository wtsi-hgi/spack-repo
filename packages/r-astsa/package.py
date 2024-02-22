# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAstsa(RPackage):
	"""Applied Statistical Time Series Analysis

	Contains data sets and scripts for analyzing time series in both the frequency and time domains including state space modeling as well as supporting the texts Time Series Analysis and Its Applications: With R Examples (5th ed coming), by R.H. Shumway and D.S. Stoffer. Springer Texts in Statistics, 2017, <DOI:10.1007/978-3-319-52452-8>, and Time Series: A Data Analysis Approach Using R. Chapman-Hall, 2019, <DOI:10.1201/9780429273285>.
	"""
	
	homepage = "https://dsstoffer.github.io/"
	cran = "astsa" 

	version("2.1", md5="29d3645e05a0d16c6d929b0fd0828859")

	depends_on("r@3.5:", type=("build", "run"))
