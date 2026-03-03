# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMultiplebubbles(RPackage):
	"""Test and Detection of Explosive Behaviors for Time Series

	Provides the Augmented Dickey-Fuller test and its variations to check the existence of bubbles (explosive behavior) for time series, based on the article by Peter C. B. Phillips, Shuping Shi and Jun Yu (2015a) <doi:10.1111/iere.12131>. Some functions may take a while depending on the size of the data used, or the number of Monte Carlo replications applied.
	"""
	
	cran = "MultipleBubbles" 

	version("0.2.0", md5="1d0d831e8f65ea96c59ab4e4b3e58794")

	depends_on("r-mass@7.3:", type=("build", "run"))
	depends_on("r-foreach@1.4.4:", type=("build", "run"))
