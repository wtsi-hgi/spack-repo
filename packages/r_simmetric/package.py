# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSimmetric(RPackage):
	"""Metrics (with Uncertainty) for Simulation Studies that Evaluate
Statistical Methods

	Allows users to quickly apply individual or multiple metrics to evaluate Monte Carlo simulation studies.
	"""
	
	cran = "simMetric" 

	version("0.1.1", md5="ce2cda59e8c43a4419629ecce921a587")

	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
