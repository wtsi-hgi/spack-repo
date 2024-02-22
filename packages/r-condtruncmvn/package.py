# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCondtruncmvn(RPackage):
	"""Conditional Truncated Multivariate Normal Distribution

	Computes the density and probability for the conditional truncated multivariate normal (Horrace (2005) p. 4, <doi:10.1016/j.jmva.2004.10.007>). Also draws random samples from this distribution.
	"""
	
	cran = "condTruncMVN" 

	version("0.0.2", md5="63a2e1b5e763548f291b0d63d0acbc3c")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-condmvnorm@2020.1:", type=("build", "run"))
	depends_on("r-matrixnormal@0.0.1:", type=("build", "run"))
	depends_on("r-tmvmixnorm@1.0.2:", type=("build", "run"))
	depends_on("r-tmvtnorm@1.4.10:", type=("build", "run"))
	depends_on("r-truncnorm@1.0.8:", type=("build", "run"))
