# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REl(RPackage):
	"""Two-Sample Empirical Likelihood

	Empirical likelihood (EL) inference for two-sample problems. The following statistics are included: the difference of two-sample means, smooth Huber estimators, quantile (qdiff) and cumulative distribution functions (ddiff), probability-probability (P-P) and quantile-quantile (Q-Q) plots as well as receiver operating characteristic (ROC) curves. EL calculations are based on J. Valeinis, E. Cers (2011) <http://home.lu.lv/~valeinis/lv/petnieciba/EL_TwoSample_2011.pdf>.
	"""
	
	cran = "EL" 

	version("1.2", md5="e80ef832ee0e9385501a457e7dedb7aa")

