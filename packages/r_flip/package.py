# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFlip(RPackage):
	"""Multivariate Permutation Tests

	It implements many univariate and multivariate permutation (and
    rotation) tests. Allowed tests: the t one and two samples, ANOVA, linear
    models, Chi Squared test, rank tests (i.e. Wilcoxon, Mann-Whitney,
    Kruskal-Wallis), Sign test and Mc Nemar. Test on Linear Models are
    performed also in presence of covariates (i.e. nuisance parameters).
    The permutation and the rotation methods to get the null distribution of
    the test statistics are available. It also implements methods for
    multiplicity control such as Westfall & Young minP procedure and Closed
    Testing (Marcus, 1976) and k-FWER. Moreover, it allows to test for fixed
    effects in mixed effects models.
	"""
	
	homepage = "ttps://CRAN.R-project.org/package=flip"
	cran = "flip" 

	version("2.5.0", md5="612106824f9fe903ad32cf330cce08f0")

	depends_on("r-cherry", type=("build", "run"))
	depends_on("r-e1071", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-somemtp", type=("build", "run"))
