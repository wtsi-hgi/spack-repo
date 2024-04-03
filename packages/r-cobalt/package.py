# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCobalt(RPackage):
	"""Covariate Balance Tables and Plots

	Generate balance tables and plots for covariates of groups preprocessed through 
             matching, weighting or subclassification, for example, using propensity scores. Includes 
             integration with 'MatchIt', 'WeightIt', 'MatchThem', 'twang', 'Matching', 'optmatch', 'CBPS', 'ebal', 
             'cem', 'sbw', and 'designmatch' for assessing balance on the output of their preprocessing 
             functions. Users can also specify data for balance assessment not generated through 
             the above packages. Also included are methods for assessing balance in clustered or 
             multiply imputed data sets or data sets with multi-category, continuous, or longitudinal treatments.
	"""
	
	homepage = "https://ngreifer.github.io/cobalt/"
	cran = "cobalt" 

	version("4.5.4", md5="b94f1e26474d5fe064590d77178c104a")
	version("4.5.5", md5="499150ab6acc04a7b60db5ddc0a063ec")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-ggplot2@3.4.1:", type=("build", "run"))
	depends_on("r-gtable@0.3:", type=("build", "run"))
	depends_on("r-gridextra@2.3:", type=("build", "run"))
	depends_on("r-chk@0.8.1:", type=("build", "run"))
	depends_on("r-rlang@0.4:", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
	depends_on("r-backports@1.1.9:", type=("build", "run"))
