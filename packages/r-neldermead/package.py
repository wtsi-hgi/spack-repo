# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNeldermead(RPackage):
	"""R Port of the 'Scilab' Neldermead Module

	Provides several direct search optimization algorithms based on the
  simplex method. The provided algorithms are direct search algorithms, i.e.
  algorithms which do not use the derivative of the cost function. They are
  based on the update of a simplex. The following algorithms are available: the
  fixed shape simplex method of Spendley, Hext and Himsworth (unconstrained
  optimization with a fixed shape simplex, 1962) <doi:10.1080/00401706.1962.10490033>, 
  the variable shape simplex method of Nelder and Mead (unconstrained optimization
  with a variable shape simplex made, 1965) <doi:10.1093/comjnl/7.4.308>, and 
  Box's complex method (constrained optimization with a variable shape simplex,
  1965) <doi: 10.1093/comjnl/8.1.42>.
	"""
	
	cran = "neldermead" 

	version("1.0-12", md5="a5df4a9edd6c7ba2b7b3821d407cdeeb")

	depends_on("r-optimbase@1.0.9:", type=("build", "run"))
	depends_on("r-optimsimplex@1.0.7:", type=("build", "run"))
