# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTransmdl(RPackage):
	"""Semiparametric Transformation Models

	To make the semiparametric transformation models easier to apply in real studies, 
    we introduce this R package, in which the MLE in transformation models via 
    an EM algorithm proposed by Zeng D, Lin DY(2007) <doi:10.1111/j.1369-7412.2007.00606.x> 
    and adaptive lasso method in transformation models proposed by Liu XX, Zeng 
    D(2013) <doi:10.1093/biomet/ast029> are implemented.  
    C++ functions are used to compute complex loops. The coefficient vector and 
    cumulative baseline hazard function can be estimated, along with the 
    corresponding standard errors and P values.
	"""
	
	cran = "transmdl" 

	version("0.1.0", md5="02e8e91aff3991098e03f501fea11fcb")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-statmod", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
