# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMratios(RPackage):
	"""Ratios of Coefficients in the General Linear Model

	Performs (simultaneous) inferences for ratios of linear combinations of coefficients in the general linear model, linear mixed model, and for quantiles in a one-way layout. Multiple comparisons and simultaneous confidence interval estimations can be performed for ratios of treatment means in the normal one-way layout with homogeneous and heterogeneous treatment variances, according to Dilba et al. (2007) <https://cran.r-project.org/doc/Rnews/Rnews_2007-1.pdf> and Hasler and Hothorn (2008) <doi:10.1002/bimj.200710466>. Confidence interval estimations for ratios of linear combinations of linear model parameters like in (multiple) slope ratio and parallel line assays can be carried out. Moreover, it is possible to calculate the sample sizes required in comparisons with a control based on relative margins. For the simple two-sample problem, functions for a t-test for ratio-formatted hypotheses and the corresponding confidence interval are provided assuming homogeneous or heterogeneous group variances.
	"""
	
	cran = "mratios" 

	version("1.4.2", md5="d149775b424e2540090aa039867effe2")

	depends_on("r@2.12:", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-multcomp", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-survpresmooth", type=("build", "run"))
