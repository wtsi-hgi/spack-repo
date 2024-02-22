# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSurvtrunc(RPackage):
	"""Analysis of Doubly Truncated Data

	Package performs Cox regression and survival distribution function estimation when the survival times are subject to double truncation. In case that the survival and truncation times are quasi-independent, the estimation procedure for each method involves inverse probability weighting, where the weights correspond to the inverse of the selection probabilities and are estimated using the survival times and truncation times only. A test for checking this independence assumption is also included in this package. The functions available in this package for Cox regression, survival distribution function estimation, and testing independence under double truncation are based on the following methods, respectively: Rennert and Xie (2018) <doi:10.1111/biom.12809>, Shen (2010) <doi:10.1007/s10463-008-0192-2>, Martin and Betensky (2005) <doi:10.1198/016214504000001538>. When the survival times are dependent on at least one of the truncation times, an EM algorithm is employed to obtain point estimates for the regression coefficients. The standard errors are calculated using the bootstrap method. See Rennert and Xie (2022) <doi:10.1111/biom.13451>. Both the independent and dependent cases assume no censoring is present in the data. Please contact Lior Rennert <liorr@clemson.edu> for questions regarding function coxDT and Yidan Shi <yidan.shi@pennmedicine.upenn.edu> for questions regarding function coxDTdep.  
	"""
	
	cran = "SurvTrunc" 

	version("0.2.0", md5="aab1609b1e045d55ae9c2a81f99b9087")

	depends_on("r-survival", type=("build", "run"))
