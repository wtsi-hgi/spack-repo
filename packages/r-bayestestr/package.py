# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBayestestr(RPackage):
	"""Understand and Describe Bayesian Models and Posterior
Distributions

	Provides utilities to describe posterior
    distributions and Bayesian models. It includes point-estimates such as
    Maximum A Posteriori (MAP), measures of dispersion (Highest Density
    Interval - HDI; Kruschke, 2015 <doi:10.1016/C2012-0-00477-2>) and
    indices used for null-hypothesis testing (such as ROPE percentage, pd
    and Bayes factors). References: Makowski et al. (2021) <doi:10.21105/joss.01541>.
	"""
	
	homepage = "https://easystats.github.io/bayestestR/"
	cran = "bayestestR" 

	version("0.13.2", md5="85cc8355c9f46c7ef258766730cef366")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-insight@0.19.8:", type=("build", "run"))
	depends_on("r-datawizard@0.9.1:", type=("build", "run"))
