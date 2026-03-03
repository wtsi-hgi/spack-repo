# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REvgam(RPackage):
	"""Generalised Additive Extreme Value Models

	Methods for fitting various extreme value distributions with parameters of 
      generalised additive model (GAM) form are provided. For details of distributions 
      see Coles, S.G. (2001) <doi:10.1007/978-1-4471-3675-0>, GAMs see Wood, S.N. (2017) 
      <doi:10.1201/9781315370279>, and the fitting approach see Wood, S.N., Pya, N. & 
      Safken, B. (2016) <doi:10.1080/01621459.2016.1180986>. Details of how evgam works
      and various examples are given in Youngman, B.D. (2022) <doi:10.18637/jss.v103.i03>.
	"""
	
	cran = "evgam" 

	version("1.0.0", md5="36550826543d48b0ed258710110d2ecb")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
