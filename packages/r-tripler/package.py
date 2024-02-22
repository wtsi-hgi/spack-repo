# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTripler(RPackage):
	"""Social Relation Model (SRM) Analyses for Single or Multiple
Groups

	Social Relation Model (SRM) analyses for single or multiple
    round-robin groups are performed. These analyses are either based on one
    manifest variable, one latent construct measured by two manifest variables,
    two manifest variables and their bivariate relations, or two latent
    constructs each measured by two manifest variables. Within-group t-tests
    for variance components and covariances are provided for single groups.
    For multiple groups two types of significance tests are provided:
    between-groups t-tests (as in SOREMO) and enhanced standard errors based on
    Lashley and Bond (1997) <DOI:10.1037/1082-989X.2.3.278>. Handling for missing values is provided.
	"""
	
	cran = "TripleR" 

	version("1.5.4", md5="32d49d6341db95357d63796c35b0103b")

	depends_on("r-ggplot2@0.9.3:", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
