# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RJointmeancov(RPackage):
	"""Joint Mean and Covariance Estimation for Matrix-Variate Data

	Jointly estimates two-group means and covariances
    for matrix-variate data and calculates test statistics.  
    This package implements the algorithms defined in 
    Hornstein, Fan, Shedden, and Zhou (2018) 
    <doi:10.1080/01621459.2018.1429275>.  
	"""
	
	cran = "jointMeanCov" 

	version("0.1.0", md5="c38e1226172c0309fa5233da0db57d21")

	depends_on("r-glasso", type=("build", "run"))
