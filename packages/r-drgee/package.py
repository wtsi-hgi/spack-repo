# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDrgee(RPackage):
	"""Doubly Robust Generalized Estimating Equations

	Fit restricted mean models for the conditional association
  between an exposure and an outcome, given covariates. Three methods
  are implemented: O-estimation, where a nuisance model for the
  association between the covariates and the outcome is used;
  E-estimation where a nuisance model for the association
  between the covariates and the exposure is used, and doubly robust (DR)
  estimation where both nuisance models are used. In DR-estimation,
  the estimates will be consistent when at least one of the nuisance
  models is correctly specified, not necessarily both. For more information, see Zetterqvist and Sjölander (2015) <doi:10.1515/em-2014-0021>.
	"""
	
	cran = "drgee" 

	version("1.1.10", md5="92b76c63974397e3578553e9a3aa8687")

	depends_on("r-nleqslv", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
