# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTrafo(RPackage):
	"""Estimation, Comparison and Selection of Transformations

	Estimation, selection and comparison of several families of
 transformations. The families of transformations included in the package are 
 the following: Bickel-Doksum (Bickel and Doksum 1981 <doi:10.2307/2287831>), 
 Box-Cox, Dual (Yang 2006 <doi:10.1016/j.econlet.2006.01.011>), 
 Glog (Durbin et al. 2002 <doi:10.1093/bioinformatics/18.suppl_1.S105>), 
 gpower (Kelmansky et al. 2013 <doi:10.1515/sagmb-2012-0030>), 
 Log, Log-shift opt (Feng et al. 2016 <doi:10.1002/sta4.104>),
 Manly, modulus (John and Draper 1980 <doi:10.2307/2986305>), 
 Neglog (Whittaker et al. 2005 <doi:10.1111/j.1467-9876.2005.00520.x>), 
 Reciprocal and Yeo-Johnson. The package simplifies to 
 compare linear models with untransformed and transformed dependent variable 
 as well as linear models where the dependent variable is transformed with 
 different transformations. Furthermore, the package employs maximum likelihood 
 approaches, moments optimization and divergence minimization to estimate the optimal 
 transformation parameter.
	"""
	
	cran = "trafo" 

	version("1.0.1", md5="c2fed5c8851acd4d9eb2587921888de2")

	depends_on("r@3.2.4:", type=("build", "run"))
	depends_on("r-fnn", type=("build", "run"))
	depends_on("r-moments", type=("build", "run"))
	depends_on("r-pryr", type=("build", "run"))
	depends_on("r-lmtest", type=("build", "run"))
