# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLkt(RPackage):
	"""Logistic Knowledge Tracing

	Computes Logistic Knowledge Tracing ('LKT') which is a general method for tracking human learning in an educational software system. Please see Pavlik, Eglington, and Harrel-Williams (2021) <https://ieeexplore.ieee.org/document/9616435>. 'LKT' is a method to compute features of student data that are used as predictors of subsequent performance. 'LKT' allows great flexibility in the choice of predictive components and features computed for these predictive components. The system is built on top of 'LiblineaR', which enables extremely fast solutions compared to base glm() in R.
	"""
	
	cran = "LKT" 

	version("1.6.0", md5="5a6ed89cd2e70d37d90102ea4e9a2837")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-sparsem@1.78:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-data-table@1.13.2:", type=("build", "run"))
	depends_on("r-liblinear@2.10.8:", type=("build", "run"))
	depends_on("r-glmnet@4.0.2:", type=("build", "run"))
	depends_on("r-glmnetutils@1.1.8:", type=("build", "run"))
	depends_on("r-lme4@1.1.23:", type=("build", "run"))
	depends_on("r-cluster@2.1.3:", type=("build", "run"))
	depends_on("r-proc@1.16.2:", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
	depends_on("r-hdinterval@0.2.2:", type=("build", "run"))
