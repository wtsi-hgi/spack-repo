# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMarqlevalg(RPackage):
	"""A Parallelized General-Purpose Optimization Based on
Marquardt-Levenberg Algorithm

	This algorithm provides a numerical solution to the
        problem of unconstrained local minimization (or maximization). It is particularly suited for complex problems and more efficient than
        the Gauss-Newton-like algorithm when starting from points very
        far from the final minimum (or maximum). Each iteration is parallelized and convergence relies on a stringent stopping criterion based on the first and second derivatives. See Philipps et al, 2021 <doi:10.32614/RJ-2021-089>.
	"""
	
	cran = "marqLevAlg" 

	version("2.0.8", md5="c771269b24d21b0e0acb74fc655ee5b2")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
