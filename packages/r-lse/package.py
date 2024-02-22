# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLse(RPackage):
	"""Constrained Least Squares and Generalized QR Factorization

	The solution of equality constrained least squares problem (LSE) is
    given through four analytics methods (Generalized QR Factorization, Lagrange 
    Multipliers, Direct Elimination and Null Space method). We expose the 
    orthogonal decomposition called Generalized QR Factorization (GQR) and also RQ 
    factorization. Finally some codes for the solution of LSE applied in 
    quaternions.
	"""
	
	homepage = "https://github.com/sergio05acm/LSE"
	cran = "LSE" 

	version("1.0.0", md5="3195d35a3bd3542a245b749851187a4f")

	depends_on("r-mass", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
