# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RModel4you(RPackage):
	"""Stratified and Personalised Models Based on Model-Based Trees
and Forests

	Model-based trees for subgroup analyses in clinical trials and
  model-based forests for the estimation and prediction of personalised
  treatment effects (personalised models). Currently partitioning of linear
  models, lm(), generalised linear models, glm(), and Weibull models,
  survreg(), is supported.  Advanced plotting functionality is supported for
  the trees and a test for parameter heterogeneity is provided for the
  personalised models. For details on model-based trees for subgroup analyses
  see Seibold, Zeileis and Hothorn (2016) <doi:10.1515/ijb-2015-0032>; for
  details on model-based forests for estimation of individual treatment effects
  see Seibold, Zeileis and Hothorn (2017) <doi:10.1177/0962280217693034>.
	"""
	
	cran = "model4you" 

	version("0.9-7", md5="5e3ce57f17144192fe1dc9f37e29624a")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-partykit@1.2.6:", type=("build", "run"))
	depends_on("r-sandwich", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-formula", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
