# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMeboot(RPackage):
	"""Maximum Entropy Bootstrap for Time Series

	Maximum entropy density based dependent data bootstrap. 
  An algorithm is provided to create a population of time series (ensemble) 
  without assuming stationarity. The reference paper (Vinod, H.D., 2004 <DOI: 10.1016/j.jempfin.2003.06.002>) explains
  how the algorithm satisfies the ergodic theorem and the central limit theorem.
	"""
	
	cran = "meboot" 

	version("1.4-9.4", md5="28500d4ae2fa61a468c0fd1dbc1506df")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dynlm", type=("build", "run"))
	depends_on("r-nlme", type=("build", "run"))
	depends_on("r-tdigest", type=("build", "run"))
	depends_on("r-hdrcde", type=("build", "run"))
