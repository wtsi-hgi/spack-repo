# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCifinder(RPackage):
	"""Estimate the Confidence Intervals for Predictive Values

	Computes confidence intervals for the positive predictive value (PPV) and negative predictive value (NPV) based on varied scenarios. In prospective studies where the proportion of diseased subjects is an unbiased estimate of the disease prevalence, this package provides several methods for calculating the confidence intervals for PPV and NPV including Clopper-Pearson, Wald, Wilson, Agresti-Coull, and Beta. In situations where the proportion of diseased subjects does not correspond to the disease prevalence (e.g. case-control studies), this package provides two types of solutions: 1) three methods for estimating confidence intervals for PPV and NPV via ratio of two binomial proportions including Gart & Nam (1988), Walter (1975), and MOVER-J (Laud, 2017); 2) three direct methods that compute the confidence intervals including Pepe (2003), Zhou (2007), and Delta. See the Details and References sections in the corresponding functions.
	"""
	
	cran = "CIfinder" 

	version("1.0.2", md5="c2757b10ad8686245b2b38815f37feea")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-ratesci", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
	depends_on("r-kableextra", type=("build", "run"))
