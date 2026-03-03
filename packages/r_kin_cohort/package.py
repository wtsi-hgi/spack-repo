# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKinCohort(RPackage):
	"""Analysis of Kin-Cohort Studies

	Analysis of kin-cohort studies. kin.cohort provides estimates of age-specific 
 cumulative risk of a disease for carriers and noncarriers of a mutation. The cohorts are
 retrospectively built from relatives of probands for whom the genotype is known. Currently 
 the method of moments and marginal maximum likelihood are implemented. Confidence intervals 
 are calculated from bootstrap samples.
 Most of the code is a translation from previous 'MATLAB' code by N. Chatterjee.
	"""
	
	cran = "kin.cohort" 

	version("0.7", md5="d9cad1c9a8ccac0f5bbdcbe077aef787")

	depends_on("r-survival", type=("build", "run"))
