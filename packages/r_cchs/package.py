# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCchs(RPackage):
	"""Cox Model for Case-Cohort Data with Stratified
Subcohort-Selection

	Contains a function, also called 'cchs', that calculates Estimator III of Borgan et al (2000), <DOI:10.1023/A:1009661900674>. This estimator is for fitting a Cox proportional hazards model to data from a case-cohort study where the subcohort was selected by stratified simple random sampling.
	"""
	
	cran = "cchs" 

	version("0.4.4", md5="70a8ffbcb131917e95c1ae3475a81403")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-survival@2.36.12:", type=("build", "run"))
