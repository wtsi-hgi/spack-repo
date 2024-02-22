# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIsmev(RPackage):
	"""An Introduction to Statistical Modeling of Extreme Values

	Functions to support the computations carried out in
  `An Introduction to Statistical Modeling of Extreme Values' by
  Stuart Coles. The functions may be divided into the following 
  groups; maxima/minima, order statistics, peaks over thresholds
  and point processes.  
	"""
	
	homepage = "http://www.ral.ucar.edu/~ericg/softextreme.php"
	cran = "ismev" 

	version("1.42", md5="35d6f5fa7f29eb822d4efad81b3dd59e")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
