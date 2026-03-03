# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHopit(RPackage):
	"""Hierarchical Ordered Probit Models with Application to Reporting
Heterogeneity

	Self-reported health, happiness, attitudes, and other statuses or perceptions are often the subject of biases that may come from different sources. For example, the evaluation of an individual’s own health may depend on previous medical diagnoses, functional status, and symptoms and signs of illness; as on well as life-style behaviors, including contextual social, gender, age-specific, linguistic and other cultural factors (Jylha 2009 <doi:10.1016/j.socscimed.2009.05.013>; Oksuzyan et al. 2019 <doi:10.1016/j.socscimed.2019.03.002>). The hopit package offers versatile functions for analyzing different self-reported ordinal variables, and for helping to estimate their biases. Specifically, the package provides the function to fit a generalized ordered probit model that regresses original self-reported status measures on two sets of independent variables (King et al. 2004 <doi:10.1017/S0003055403000881>; Jurges 2007  <doi:10.1002/hec.1134>; Oksuzyan et al. 2019  <doi:10.1016/j.socscimed.2019.03.002>). The first set of variables (e.g., health variables) included in the regression are individual statuses and characteristics that are directly related to the self-reported variable. In the case of self-reported health, these could be chronic conditions, mobility level, difficulties with daily activities, performance on grip strength tests, anthropometric measures, and lifestyle behaviors. The second set of independent variables (threshold variables) is used to model cut-points between adjacent self-reported response categories as functions of individual characteristics, such as gender, age group, education, and country (Oksuzyan et al. 2019 <doi:10.1016/j.socscimed.2019.03.002>). The model helps to adjust for specific socio-demographic and cultural differences in how the continuous latent health is projected onto the ordinal self-rated measure. The fitted model can be used to calculate an individual predicted latent status variable, a latent index, and standardized latent coefficients; and makes it possible to reclassify a categorical status measure that has been adjusted for inter-individual differences in reporting behavior.
	"""
	
	cran = "hopit" 

	version("0.11.6", md5="c4921fc4de50e3010539272bc76349bc")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-survey@4.1.1:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-questionr", type=("build", "run"))
	depends_on("r-rdpack@0.11:", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
