# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMetastan(RPackage):
	"""Bayesian Meta-Analysis via 'Stan'

	Performs Bayesian meta-analysis, meta-regression and model-based meta-analysis 
             using 'Stan'. Includes binomial-normal hierarchical models and option to use 
             weakly informative priors for the heterogeneity parameter and the treatment effect 
             parameter which are described in Guenhan, Roever, and Friede (2020) <doi:10.1002/jrsm.1370>.
	"""
	
	homepage = "https://github.com/gunhanb/MetaStan"
	cran = "MetaStan" 

	version("1.0.0", md5="efcefd3accca8c47f3f616ea86264727")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp@0.12.17:", type=("build", "run"))
	depends_on("r-rstan@2.18.1:", type=("build", "run"))
	depends_on("r-rstantools@1.5:", type=("build", "run"))
	depends_on("r-loo@2:", type=("build", "run"))
	depends_on("r-forestplot@1.6:", type=("build", "run"))
	depends_on("r-metafor@2.0.0:", type=("build", "run"))
	depends_on("r-hdinterval", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
	depends_on("r-stanheaders@2.18:", type=("build", "run"))
	depends_on("r-bh@1.66.0.1:", type=("build", "run"))
	depends_on("r-rcppeigen@0.3.3.4:", type=("build", "run"))
	depends_on("r-rcppparallel@5.0.1:", type=("build", "run"))
