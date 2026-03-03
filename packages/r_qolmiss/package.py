# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQolmiss(RPackage):
	"""Scales Score Calculation from Quality of Life Data

	There are three functions: qol, miss_qol and miss_patient takes input of the data set containing the answers of QOL questionnaire. It will compute the three types of domain based scale scores: Global, Functional, and Symptoms. In case of missing data, the miss_qol and miss_patient functions will make the required changes and then calculate the domain-wise scale scores. Finally, provide an output replacing the question columns with the domain-based scale scores in the original data set.
	"""
	
	cran = "QoLMiss" 

	version("0.1.0", md5="81f7694c94acc74ab092848977f3ef60")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-missmethods", type=("build", "run"))
