# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCompositereliability(RPackage):
	"""Determine the Composite Reliability of a Naturalistic,
Unbalanced Dataset

	The reliability of assessment tools is a crucial aspect of monitoring student performance in various educational settings. It ensures that the assessment outcomes accurately reflect a student's true level of performance. However, when assessments are combined, determining composite reliability can be challenging, especially for naturalistic and unbalanced datasets. This package provides an easy-to-use solution for calculating composite reliability for different assessment types. It allows for the inclusion of weight per assessment type and produces extensive G- and D-study results with graphical interpretations. Overall, our approach enhances the reliability of composite assessments, making it suitable for various education contexts.
	"""
	
	homepage = "https://github.com/jmoonen/CompositeReliability"
	cran = "CompositeReliability" 

	version("1.0.3", md5="c525131364b84114cc8eae692379d509")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-lme4", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-psych", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-rsolnp", type=("build", "run"))
