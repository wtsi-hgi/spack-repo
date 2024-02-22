# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPsaboot(RPackage):
	"""Bootstrapping for Propensity Score Analysis

	It is often advantageous to test a hypothesis more than once
    in the context of propensity score analysis (Rosenbaum, 2012)
    <doi:10.1093/biomet/ass032>. The functions in this package facilitate
    bootstrapping for propensity score analysis (PSA). By default,
    bootstrapping using two classification tree methods (using 'rpart' and
    'ctree' functions), two matching methods (using 'Matching' and
    'MatchIt' packages), and stratification with logistic regression.  A
    framework is described for users to implement additional propensity
    score methods.  Visualizations are emphasized for diagnosing balance;
    exploring the correlation relationships between bootstrap samples and
    methods; and to summarize results.
	"""
	
	homepage = "https://github.com/jbryer/PSAboot"
	cran = "PSAboot" 

	version("1.3.8", md5="84d829560897c98c406aba8724e09e42")

	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-psagraphics", type=("build", "run"))
	depends_on("r@3:", type=("build", "run"))
	depends_on("r-ggthemes", type=("build", "run"))
	depends_on("r-matching", type=("build", "run"))
	depends_on("r-matchit", type=("build", "run"))
	depends_on("r-modeltools", type=("build", "run"))
	depends_on("r-party", type=("build", "run"))
	depends_on("r-psych", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-rpart", type=("build", "run"))
	depends_on("r-trimatch", type=("build", "run"))
