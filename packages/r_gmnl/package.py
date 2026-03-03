# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGmnl(RPackage):
	"""Multinomial Logit Models with Random Parameters

	An implementation of maximum simulated likelihood method for the
    estimation of multinomial logit models with random coefficients as presented by Sarrias and Daziano (2017) <doi:10.18637/jss.v079.i02>.
    Specifically, it allows estimating models with continuous heterogeneity
    such as the mixed multinomial logit and the generalized multinomial logit.
    It also allows estimating models with discrete heterogeneity such as the
    latent class and the mixed-mixed multinomial logit model.
	"""
	
	homepage = "https://msarrias.com/description.html"
	cran = "gmnl" 

	version("1.1-3.2", md5="3e5ffeec37ad2a4c0a95fe32cba25f8d")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-maxlik", type=("build", "run"))
	depends_on("r-formula", type=("build", "run"))
	depends_on("r-plotrix", type=("build", "run"))
	depends_on("r-msm", type=("build", "run"))
	depends_on("r-mlogit", type=("build", "run"))
	depends_on("r-truncnorm", type=("build", "run"))
