# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCondsurv(RPackage):
	"""Estimation of the Conditional Survival Function for Ordered
Multivariate Failure Time Data

	Method to implement some newly developed methods for the
    estimation of the conditional survival function. See Meira-Machado, 
    Sestelo and Goncalves (2016) <doi:10.1002/bimj.201500038>.
	"""
	
	cran = "condSURV" 

	version("2.0.4", md5="4141f69a4189877376934a138654f99f")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-kernsmooth", type=("build", "run"))
	depends_on("r-np", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-dorng", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
