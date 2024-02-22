# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RConleyreg(RPackage):
	"""Estimations using Conley Standard Errors

	Functions calculating Conley (1999) <doi:10.1016/S0304-4076(98)00084-0> standard errors. The package started by merging and extending multiple packages and 
  other published scripts on this econometric technique. It strongly emphasizes computational optimization. Details are available in the function documentation and in 
  the vignette.
	"""
	
	cran = "conleyreg" 

	version("0.1.7", md5="3ea21eb184ce7f665b2ba2fa63893bb1")

	depends_on("r-sf", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-lmtest", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
	depends_on("r-fixest", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-lwgeom", type=("build", "run"))
	depends_on("r-s2", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
