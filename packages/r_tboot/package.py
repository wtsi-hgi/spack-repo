# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTboot(RPackage):
	"""Tilted Bootstrap

	Creates simulated clinical trial data with realistic correlation structures and assumed efficacy levels by using a tilted bootstrap resampling approach. Samples are drawn from observed data with some samples appearing more frequently than others. May also be used for simulating from a joint Bayesian distribution along with clinical trials based on the Bayesian distribution.
	"""
	
	homepage = "https://github.com/njm18/tboot"
	cran = "tboot" 

	version("0.2.1", md5="2acaaf1107518cd0598614b2e55a9af1")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-quadprog", type=("build", "run"))
	depends_on("r-kernlab", type=("build", "run"))
