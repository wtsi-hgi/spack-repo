# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPpmsuite(RPackage):
	"""A Collection of Models that Employ Product Partition
Distributions as a Prior on Partitions

	Provides a suite of functions that fit models that use PPM type priors for partitions.
                Models include hierarchical Gaussian and probit ordinal models with  a (covariate 
                dependent) PPM.  If a covariate dependent product partition model is selected, 
                then all the options detailed in Page, G.L.; Quintana, F.A. (2018) 
                <doi:10.1007/s11222-017-9777-z> are available.  If covariate values are missing, 
                then the approach detailed in Page, G.L.; Quintana, F.A.; Mueller, P (2020) 
                <doi:10.1080/10618600.2021.1999824> is employed.   Also included in the package is 
                a function that fits a Gaussian likelihood spatial product  partition model that is 
                detailed in Page, G.L.; Quintana, F.A. (2016)  <doi:10.1214/15-BA971>, and 
                multivariate PPM change point models that are detailed in Quinlan, J.J.; Page, G.L.; 
                Castro, L.M. (2023) <doi:10.1214/22-BA1344>. In addition, a function that fits a 
                univariate or bivariate functional data model that employs a PPM or a PPMx to 
                cluster curves based on B-spline coefficients is provided.
	"""
	
	cran = "ppmSuite" 

	version("0.3.4", md5="9b836fc5fe27ece9800490c58cc92c97")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
