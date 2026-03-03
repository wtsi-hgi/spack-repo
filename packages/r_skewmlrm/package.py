# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSkewmlrm(RPackage):
	"""Estimation for Scale-Shape Mixtures of Skew-Normal Distributions

	Provide data generation and estimation tools for the multivariate scale mixtures of normal 
             presented in Lange and Sinsheimer (1993) <doi:10.2307/1390698>, the multivariate scale 
             mixtures of skew-normal presented in Zeller, Lachos and Vilca (2011) 
             <doi:10.1080/02664760903406504>, the multivariate skew scale mixtures of normal 
             presented in Louredo, Zeller and Ferreira (2021) <doi:10.1007/s13571-021-00257-y>
             and the multivariate scale mixtures of skew-normal-Cauchy presented in Kahrari et al. (2020)
	     <doi:10.1080/03610918.2020.1804582>. 
	"""
	
	cran = "skewMLRM" 

	version("1.6", md5="c3118847353953619d0c2aa175da30c0")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-moments", type=("build", "run"))
	depends_on("r-clustergeneration", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-matrixcalc", type=("build", "run"))
