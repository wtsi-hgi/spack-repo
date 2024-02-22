# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTrendeval(RPackage):
	"""Evaluate Trending Models

	Provides a coherent interface for evaluating models fit with the
  trending package.  This package is part of the RECON
  (<https://www.repidemicsconsortium.org/>) toolkit for outbreak analysis.
	"""
	
	homepage = "https://github.com/reconverse/trendeval"
	cran = "trendeval" 

	version("0.1.0", md5="5678d01aa90b5c58a89f0ad6431aed5d")

	depends_on("r-trending@0.1:", type=("build", "run"))
	depends_on("r-yardstick", type=("build", "run"))
	depends_on("r-rsample", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
