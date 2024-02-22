# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIntccr(RPackage):
	"""Semiparametric Competing Risks Regression under Interval
Censoring

	Semiparametric regression models on the cumulative incidence function for interval-censored competing risks data as described in Bakoyannis, Yu, & Yiannoutsos (2017) /doi{10.1002/sim.7350} and the models with missing event types as described in Park, Bakoyannis, Zhang, & Yiannoutsos (2021) doi{10.1093/biostatistics/kxaa052}. The proportional subdistribution hazards model (Fine-Gray model), the proportional odds model, and other models that belong to the class of semiparametric generalized odds rate transformation models.
	"""
	
	cran = "intccr" 

	version("3.0.4", md5="6d884cf2983639df2ba11e7494dee762")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-alabama", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-splines2", type=("build", "run"))
