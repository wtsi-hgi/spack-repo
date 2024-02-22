# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCubature(RPackage):
	"""Adaptive multivariate integration over hypercubes.

	R wrappers around the cubature C library of Steven G. Johnson for adaptive
	multivariate integration over hypercubes and the Cuba C library of Thomas
	Hahn for deterministic and Monte Carlo integration. Scalar and vector
	interfaces for  cubature and Cuba routines are provided; the vector
	interfaces are highly recommended as demonstrated in the package
	vignette."""

	cran = "cubature"

	version("2.1.0", md5="2ba4be5bef4581b51748b04105ec4c8b")

	depends_on("r-rcpp", type=("build", "run"))

	parallel = False
