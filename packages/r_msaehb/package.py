# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMsaehb(RPackage):
	"""Multivariate Small Area Estimation using Hierarchical Bayesian
Method

	Implements area level of multivariate small area estimation using Hierarchical Bayesian method under Normal and T distribution. The 'rjags' package is employed to obtain parameter estimates. For the reference, see Rao and Molina (2015) <doi:10.1002/9781118735855>.
	"""
	
	cran = "msaeHB" 

	version("0.1.0", md5="612c35e5939b443379ce9841141f832f")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-rjags", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
