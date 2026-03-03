# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPema(RPackage):
	"""Penalized Meta-Analysis

	Conduct penalized meta-analysis, see Van Lissa, Van Erp, & Clapper
    (2023) <doi:10.31234/osf.io/6phs5>. In meta-analysis, there are
    often between-study differences. These can be coded as moderator variables,
    and controlled for using meta-regression. However, if the number of
    moderators is large relative to the number of studies, such an analysis may
    be overfit. Penalized meta-regression is useful in these cases, because
    it shrinks the regression slopes of irrelevant moderators towards zero.
	"""
	
	homepage = "https://github.com/cjvanlissa/pema"
	cran = "pema" 

	version("0.1.3", md5="d1fa3f8e2a111ba6676879539a07780a")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-rstan@2.18.1:", type=("build", "run"))
	depends_on("r-rcpp@0.12:", type=("build", "run"))
	depends_on("r-rcppparallel@5.0.1:", type=("build", "run"))
	depends_on("r-rstantools@2.1.1:", type=("build", "run"))
	depends_on("r-sn", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-bh@1.66:", type=("build", "run"))
	depends_on("r-rcppeigen@0.3.3.3:", type=("build", "run"))
	depends_on("r-stanheaders@2.18:", type=("build", "run"))
