# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGlinternet(RPackage):
	"""Learning Interactions via Hierarchical Group-Lasso
Regularization

	Group-Lasso INTERaction-NET. Fits linear pairwise-interaction models that satisfy strong hierarchy: if an interaction coefficient is estimated to be nonzero, then its two associated main effects also have nonzero estimated coefficients. Accommodates categorical variables (factors) with arbitrary numbers of levels, continuous variables, and combinations thereof. Implements the machinery described in the paper "Learning interactions via hierarchical group-lasso regularization" (JCGS 2015, Volume 24, Issue 3). Michael Lim & Trevor Hastie (2015) <DOI:10.1080/10618600.2014.938812>.
	"""
	
	homepage = "http://web.stanford.edu/~hastie/Papers/glinternet_jcgs.pdf"
	cran = "glinternet" 

	version("1.0.12", md5="2c1369bdfc0264c9109459726d70c0f3")

