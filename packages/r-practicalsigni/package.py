# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPracticalsigni(RPackage):
	"""Practical Significance Ranking of Regressors and Exact t Density

	Consider a possibly nonlinear nonparametric regression
   with p regressors. We provide evaluations by 13 methods to rank
   regressors by their practical significance or importance using 
   various methods, including machine learning tools. Comprehensive
   methods are as follows. 
   m6=Generalized partial correlation coefficient or
   GPCC by Vinod (2021)<doi:10.1007/s10614-021-10190-x> and
   Vinod (2022)<https://www.mdpi.com/1911-8074/15/1/32>.
   m7= a generalization of psychologists' effect size incorporating 
   nonlinearity and many variables.
   m8= local linear partial (dy/dxi) using the 'np' package for kernel 
   regressions.
   m9= partial (dy/dxi) using the 'NNS' package.
   m10= importance measure using the 'NNS' boost function.
   m11= Shapley Value measure of importance (cooperative game theory).
   m12 and m13= two versions of the random forest algorithm.
   Taraldsen's exact density for sampling distribution of correlations added.
	"""
	
	cran = "practicalSigni" 

	version("0.1.2", md5="c3baa7eb544dd26f5277b69ea33c215c")

	depends_on("r@4.3:", type=("build", "run"))
	depends_on("r-np@0.60:", type=("build", "run"))
	depends_on("r-generalcorr@1.2:", type=("build", "run"))
	depends_on("r-xtable@1.8.4:", type=("build", "run"))
	depends_on("r-shapleyvalue@0.2:", type=("build", "run"))
	depends_on("r-nns@0.9:", type=("build", "run"))
	depends_on("r-randomforest@4.7:", type=("build", "run"))
	depends_on("r-hypergeo@1.2.13:", type=("build", "run"))
