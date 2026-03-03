# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDsrtest(RPackage):
	"""Tests and Confidence Intervals on Directly Standardized Rates
for Several Methods

	Perform a test of a simple null hypothesis about a 
    directly standardized rate and obtain the matching confidence 
    interval using a choice of methods.
	"""
	
	homepage = "https://github.com/mnelsonr/dsrTest"
	cran = "dsrTest" 

	version("1.0.0", md5="2f12bce02157f593359b142959c6acac")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-exactci", type=("build", "run"))
	depends_on("r-asht@0.9.1:", type=("build", "run"))
	depends_on("r-loglognorm", type=("build", "run"))
