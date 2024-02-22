# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDtd(RPackage):
	"""Distance to Default

	Provides fast methods to work with Merton's distance to default 
  model introduced in Merton (1974) <doi:10.1111/j.1540-6261.1974.tb03058.x>. 
  The methods includes simulation and estimation of the parameters.
	"""
	
	cran = "DtD" 

	version("0.2.2", md5="2e99464ada90d950c5cd322ac09d2a98")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
