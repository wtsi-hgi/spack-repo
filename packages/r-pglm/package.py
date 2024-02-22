# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPglm(RPackage):
	"""Panel Generalized Linear Models

	Estimation of panel models for glm-like models:
             this includes binomial models (logit and probit), count models (poisson and negbin)
	     and ordered models (logit and probit), as described in:
             Baltagi (2013) Econometric Analysis of Panel Data, ISBN-13:978-1-118-67232-7,
	     Hsiao (2014) Analysis of Panel Data  <doi:10.1017/CBO9781139839327> and
	     Croissant and Millo (2018), Panel Data Econometrics with R, ISBN:978-1-118-94918-4.
	"""
	
	homepage = "https://cran.r-project.org/package=pglm"
	cran = "pglm" 

	version("0.2-3", md5="d3bda0afc3083de2319b266b82e70388")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-maxlik", type=("build", "run"))
	depends_on("r-plm", type=("build", "run"))
	depends_on("r-statmod", type=("build", "run"))
	depends_on("r-formula", type=("build", "run"))
