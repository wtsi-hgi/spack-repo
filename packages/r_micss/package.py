# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMicss(RPackage):
	"""Modified Iterative Cumulative Sum of Squares Algorithm

	Companion package of Carrion-i-Silvestre & Sansó (2023): 
  "Generalized Extreme Value Approximation to the CUMSUMQ Test for Constant 
  Unconditional Variance in Heavy-Tailed Time Series". It implements the Modified 
  Iterative Cumulative Sum of Squares Algorithm, which is an extension of 
  the Iterative Cumulative Sum of Squares (ICSS) Algorithm of Inclan and Tiao (1994), and it checks for changes in the 
  unconditional variance of a time series controlling for the tail index of 
  the underlying distribution. The fourth order moment is estimated non-parametrically
  to avoid the size problems when the innovations are non-Gaussian (see, Sansó et al., 2004). 
  Critical values and p-values are generated using a Generalized Extreme Value distribution approach.
  References
  Carrion-i-Silvestre J.J & Sansó A (2023) <https://www.ub.edu/irea/working_papers/2023/202309.pdf>.
  Inclan C & Tiao G.C (1994) <doi:10.1080/01621459.1994.10476824>,
  Sansó A & Aragó V & Carrion-i-Silvestre J.L (2004) <https://dspace.uib.es/xmlui/bitstream/handle/11201/152078/524035.pdf>.
	"""
	
	cran = "micss" 

	version("0.1.5", md5="1d5cbf53fbbe7ba84dd98e5e596acfcb")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
