# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMrtsamplesize(RPackage):
	"""A Sample Size Calculator for Micro-Randomized Trials

	Provide a sample size calculator for micro-randomized trials (MRTs) based on methodology developed in Sample Size Calculations for Micro-randomized Trials in mHealth by Liao et al. (2016) <DOI:10.1002/sim.6847>.
	"""
	
	cran = "MRTSampleSize" 

	version("0.3.0", md5="8214a42bc2de996035550543c5ae3bab")

	depends_on("r@2.15:", type=("build", "run"))
