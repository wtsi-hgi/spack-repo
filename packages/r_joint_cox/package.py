# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RJointCox(RPackage):
	"""Joint Frailty-Copula Models for Tumour Progression and Death in
Meta-Analysis

	Fit survival data and perform dynamic prediction under joint frailty-copula models for tumour progression and death.
 Likelihood-based methods are employed for estimating model parameters, where the baseline hazard functions are modeled by the cubic M-spline or the Weibull model.
 The methods are applicable for meta-analytic data containing individual-patient information from several studies.
 Survival outcomes need information on both terminal event time (e.g., time-to-death) and non-terminal event time (e.g., time-to-tumour progression).
 Methodologies were published in
 Emura et al. (2017) <doi:10.1177/0962280215604510>, Emura et al. (2018) <doi:10.1177/0962280216688032>,
 Emura et al. (2020) <doi:10.1177/0962280219892295>, Shinohara et al. (2020) <doi:10.1080/03610918.2020.1855449>,
 Wu et al. (2020) <doi:10.1007/s00180-020-00977-1>, and Emura et al. (2021) <doi:10.1177/09622802211046390>.
 See also the book of Emura et al. (2019) <doi:10.1007/978-981-13-3516-7>.
 Survival data from ovarian cancer patients are also available.
	"""
	
	cran = "joint.Cox" 

	version("3.16", md5="735162ef3b90b7cbecac54d9aa0032a9")

	depends_on("r-survival", type=("build", "run"))
