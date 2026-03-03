# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSensitivitymw(RPackage):
	"""Sensitivity Analysis for Observational Studies Using Weighted
M-Statistics

	Sensitivity analysis for tests, confidence intervals and estimates in matched observational studies with one or more controls using weighted or unweighted Huber-Maritz M-tests (including the permutational t-test).   The method is from Rosenbaum (2014) Weighted M-statistics with superior design sensitivity in matched observational studies with multiple controls JASA, 109(507), 1145-1158 <doi:10.1080/01621459.2013.879261>.
	"""
	
	cran = "sensitivitymw" 

	version("2.1", md5="d96d919fa17ed3db2bbbf3efb5cdb68b")

	depends_on("r@3.5:", type=("build", "run"))
