# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSplitreg(RPackage):
	"""Split Regularized Regression

	Functions for computing split regularized estimators defined in Christidis, Lakshmanan, 
             Smucler and Zamar (2019) <arXiv:1712.03561>. The approach fits linear regression models that
             split the set of covariates into groups. The optimal split of the variables into groups and the 
             regularized estimation of the regression coefficients are performed by minimizing  an objective 
             function that encourages sparsity within each group and diversity among them. 
             The estimated coefficients are then pooled together to form the final fit.
	"""
	
	cran = "SplitReg" 

	version("1.0.2", md5="61c53cf27345fbc75f576b0db06595ca")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
