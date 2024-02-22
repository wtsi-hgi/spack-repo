# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStmgp(RPackage):
	"""Rapid and Accurate Genetic Prediction Modeling for Genome-Wide
Association or Whole-Genome Sequencing Study Data

	Rapidly build accurate genetic prediction models for genome-wide association or whole-genome sequencing study data by smooth-threshold multivariate genetic prediction (STMGP) method. Variable selection is performed using marginal association test p-values with an optimal p-value cutoff selected by Cp-type criterion. Quantitative and binary traits are modeled respectively via linear and logistic regression models. A function that works through PLINK software (Purcell et al. 2007 <DOI:10.1086/519795>, Chang et al. 2015 <DOI:10.1186/s13742-015-0047-8>) <https://www.cog-genomics.org/plink2> is provided. Covariates can be included in regression model.
	"""
	
	cran = "stmgp" 

	version("1.0.4", md5="e835bfd41e38c25ec0110ea20a2491ab")

	depends_on("r-mass", type=("build", "run"))
	depends_on("plink", type=("build", "link", "run"))
