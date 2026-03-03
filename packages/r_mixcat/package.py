# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMixcat(RPackage):
	"""Mixed Effects Cumulative Link and Logistic Regression Models

	Mixed effects cumulative and baseline logit link models for the analysis of ordinal or nominal responses, with non-parametric distribution for the random effects.
	"""
	
	cran = "mixcat" 

	version("1.0-4", md5="aad3341c1297d38c66bb15f69222be4d")

	depends_on("r@2.8.1:", type=("build", "run"))
	depends_on("r-statmod", type=("build", "run"))
	depends_on("gsl", type=("build", "link", "run"))
