# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRlrsim(RPackage):
	"""Exact (Restricted) Likelihood Ratio Tests for Mixed and Additive
Models

	Rapid, simulation-based exact (restricted) likelihood ratio tests
    for testing the presence of variance components/nonparametric terms for
    models fit with nlme::lme(),lme4::lmer(), lmeTest::lmer(), gamm4::gamm4(),
    mgcv::gamm() and SemiPar::spm().
	"""
	
	homepage = "https://github.com/fabian-s/RLRsim"
	cran = "RLRsim" 

	version("3.1-8", md5="113402cc72224601ebd89659b15f2223")

	depends_on("r@2.14:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-lme4@1.1:", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
	depends_on("r-nlme", type=("build", "run"))
