# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RValidateit(RPackage):
	"""Validating Topic Coherence and Topic Labels

	By creating crowd-sourcing tasks that can be easily posted and results retrieved using Amazon's Mechanical Turk (MTurk) API, researchers can use this solution to validate the quality of topics obtained from unsupervised or semi-supervised learning methods, and the relevance of topic labels assigned. This helps ensure that the topic modeling results are accurate and useful for research purposes. See Ying and others (2022) <doi:10.1101/2023.05.02.538599>. For more information, please visit <https://github.com/Triads-Developer/Topic_Model_Validation>.  
	"""
	
	cran = "validateIt" 

	version("1.2.1", md5="3d6d2a845d8b7565798764cff383c0b3")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-pymturkr", type=("build", "run"))
	depends_on("r-rlang@0.4.11:", type=("build", "run"))
	depends_on("r-tm@0.7.11:", type=("build", "run"))
	depends_on("r-here", type=("build", "run"))
	depends_on("r-snowballc", type=("build", "run"))
