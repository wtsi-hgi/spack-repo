# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHctr(RPackage):
	"""Higher Criticism Tuned Regression

	A novel searching scheme for tuning parameter in high-dimensional 
             penalized regression. We propose a new estimate of the regularization
             parameter based on an estimated lower bound of the proportion of false 
             null hypotheses (Meinshausen and Rice (2006) <doi:10.1214/009053605000000741>).
             The bound is estimated by applying the empirical null distribution of the higher 
             criticism statistic, a second-level significance testing, which is constructed
             by dependent p-values from a multi-split regression and aggregation method
             (Jeng, Zhang and Tzeng (2019) <doi:10.1080/01621459.2018.1518236>). An estimate 
             of tuning parameter in penalized regression is decided corresponding to the lower 
             bound of the proportion of false null hypotheses. Different penalized 
             regression methods are provided in the multi-split algorithm. 
	"""
	
	cran = "HCTR" 

	version("0.1.1", md5="6cb5960b2229aa9bbad421c566611ed3")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-glmnet@2.0.18:", type=("build", "run"))
	depends_on("r-harmonicmeanp@3:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-ncvreg@3.11.1:", type=("build", "run"))
	depends_on("r-rdpack@0.11.0:", type=("build", "run"))
