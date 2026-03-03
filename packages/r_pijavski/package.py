# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPijavski(RPackage):
	"""Global Univariate Minimization

	Global univariate minimization of Lipschitz functions is performed by using Pijavski method, which was published in Pijavski (1972) <DOI:10.1016/0041-5553(72)90115-2>.
	"""
	
	cran = "Pijavski" 

	version("1.0.3", md5="2356d96e1607a4a04dac4efb98e8a296")

	depends_on("r-rcpp", type=("build", "run"))
