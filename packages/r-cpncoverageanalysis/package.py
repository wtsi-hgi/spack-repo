# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCpncoverageanalysis(RPackage):
	"""Conceptual Properties Norming Studies as Parameter Estimation

	Implementation of conceptual properties norming studies, including estimates of CPNs parameters with their corresponding variances and estimates for the sampling process, and a sampling property function based on a modified empirical distribution from the original data.
	"""
	
	cran = "CPNCoverageAnalysis" 

	version("1.1.0", md5="b438df6a51f975438dd039ea13bdeac0")

	depends_on("r@2.10:", type=("build", "run"))
