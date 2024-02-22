# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBeanz(RPackage):
	"""Bayesian Analysis of Heterogeneous Treatment Effect

	It is vital to assess the heterogeneity of treatment effects
    (HTE) when making health care decisions for an individual patient or a group
    of patients. Nevertheless, it remains challenging to evaluate HTE based
    on information collected from clinical studies that are often designed and
    conducted to evaluate the efficacy of a treatment for the overall population.
    The Bayesian framework offers a principled and flexible approach to estimate
    and compare treatment effects across subgroups of patients defined by their
    characteristics. This package allows users to explore a wide range of Bayesian
    HTE analysis models, and produce posterior inferences about HTE. See Wang et al.
    (2018) <DOI:10.18637/jss.v085.i07> for further details.
	"""
	
	cran = "beanz" 

	version("3.1", md5="21e5800daf8923fb595ca3c917eb9ea4")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-rcpp@0.12:", type=("build", "run"))
	depends_on("r-rstan@2.18.1:", type=("build", "run"))
	depends_on("r-rstantools@1.5:", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-loo", type=("build", "run"))
	depends_on("r-rcppparallel@5.0.1:", type=("build", "run"))
	depends_on("r-stanheaders@2.18:", type=("build", "run"))
	depends_on("r-bh@1.66:", type=("build", "run"))
	depends_on("r-rcppeigen@0.3.3.3:", type=("build", "run"))
