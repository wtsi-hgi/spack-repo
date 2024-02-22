# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REvt0(RPackage):
	"""Mean of Order P, Peaks over Random Threshold Hill and High
Quantile Estimates

	The R package proposes extreme value index estimators for heavy tailed models 
             by mean of order p <DOI:10.1016/j.csda.2012.07.019>, peaks over random threshold
             <DOI:10.57805/revstat.v4i3.37> and a bias-reduced estimator 
             <DOI:10.1080/00949655.2010.547196>.
	     The package also computes moment, generalised Hill <DOI:10.2307/3318416> 
	     and mixed moment estimates for the extreme value index.
	     High quantiles and value at risk estimators based on these estimators are implemented.
	"""
	
	cran = "evt0" 

	version("1.1-4", md5="c852aeda5f8f7bc88566a9bd77c040d2", url="https://cran.r-project.org/src/contrib/evt0_1.1-4.tar.gz")

	depends_on("r@1.9:", type=("build", "run"))
	depends_on("r-evd", type=("build", "run"))
