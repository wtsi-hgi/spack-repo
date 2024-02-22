# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCta(RPackage):
	"""Contingency Table Analysis Based on ML Fitting of MPH Models

	Contingency table analysis is performed based on maximum likelihood (ML) fitting of 
             multinomial-Poisson homogeneous (MPH) and homogeneous linear predictor (HLP) models. 
             See Lang (2004) <doi:10.1214/aos/1079120140> and Lang (2005) <doi:10.1198/016214504000001042> 
             for MPH and HLP models. Objects computed include model goodness-of-fit statistics; likelihood-
             based (cell- and link-specific) residuals; and cell probability and expected count estimates along 
             with standard errors. This package can also compute test-inversion--e.g. Wald, profile likelihood, 
             score, power-divergence--confidence intervals for contingency table estimands, when table 
             probabilities are potentially subject to equality constraints. For test-inversion intervals, see 
             Lang (2008) <doi:10.1002/sim.3391> and Zhu (2020) <doi:10.17077/etd.005331>.
	"""
	
	cran = "cta" 

	version("1.3.0", md5="8dbc1e0a551bc9722f5a771167cbf397")

	depends_on("r-intervals", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
	depends_on("r-limsolve", type=("build", "run"))
