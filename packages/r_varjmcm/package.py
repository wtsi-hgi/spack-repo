# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVarjmcm(RPackage):
	"""Estimations for the Covariance of Estimated Parameters in Joint
Mean-Covariance Models

	The goal of the package is to equip the 'jmcm' package (current version 0.2.1) 
    with estimations of the covariance of estimated parameters. Two methods are provided. 
    The first method is to use the inverse of estimated Fisher's information matrix, see 
    M. Pourahmadi (2000) <doi:10.1093/biomet/87.2.425>, M. Maadooliat, M. Pourahmadi and 
    J. Z. Huang (2013) <doi:10.1007/s11222-011-9284-6>, and W. Zhang, C. Leng, C. Tang (2015) 
    <doi:10.1111/rssb.12065>. The second method is bootstrap based, see Liu, R.Y. (1988) 
    <doi:10.1214/aos/1176351062> for reference. 
	"""
	
	cran = "varjmcm" 

	version("0.1.1", md5="3ee215e4aca29cd30f28b44cd17ef4be")

	depends_on("r-jmcm", type=("build", "run"))
	depends_on("r-expm", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
