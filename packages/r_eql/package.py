# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REql(RPackage):
	"""Extended-Quasi-Likelihood-Function (EQL)

	Computation of the EQL for a given family of variance
        functions, Saddlepoint-approximations and related auxiliary
        functions (e.g. Hermite polynomials).
	"""
	
	cran = "EQL" 

	version("1.0-1", md5="84a0f6fc514ae0b4328913bc51959d8c")

	depends_on("r-ttutils@0.1.0:", type=("build", "run"))
	depends_on("r-lattice@0.17.17:", type=("build", "run"))
