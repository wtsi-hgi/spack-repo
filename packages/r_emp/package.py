# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REmp(RPackage):
	"""Expected Maximum Profit Classification Performance Measure

	Functions for estimating EMP (Expected Maximum Profit Measure) in Credit Risk Scoring and Customer Churn Prediction, according to Verbraken et al (2013, 2014) <DOI:10.1109/TKDE.2012.50>, <DOI:10.1016/j.ejor.2014.04.001>.
	"""
	
	cran = "EMP" 

	version("2.0.5", md5="2b79ffd577145bc178ebacf41cc7db8f")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-rocr", type=("build", "run"))
