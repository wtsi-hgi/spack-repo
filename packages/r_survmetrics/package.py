# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSurvmetrics(RPackage):
	"""Predictive Evaluation Metrics in Survival Analysis

	An implementation of popular evaluation metrics that are commonly used in survival prediction 
  including Concordance Index, Brier Score, Integrated Brier Score, 
  Integrated Square Error, Integrated Absolute Error and Mean Absolute Error.
  For a detailed information, see (Ishwaran H, Kogalur UB, Blackstone EH and Lauer MS (2008) <doi:10.1214/08-AOAS169>) and
  (Moradian H, Larocque D and Bellavance F (2017) <doi:10.1007/s10985-016-9372-1>) for different evaluation metrics.
	"""
	
	homepage = "https://github.com/skyee1/SurvMetrics"
	cran = "SurvMetrics" 

	version("0.5.0", md5="1b4868aec171255036d7f2f22304b46f")

	depends_on("r-survminer", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-pec", type=("build", "run"))
	depends_on("r-randomforestsrc", type=("build", "run"))
