# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPolyapost(RPackage):
	"""Simulating from the Polya Posterior

	Simulate via Markov chain Monte Carlo (hit-and-run algorithm)
    a Dirichlet distribution conditioned to satisfy a finite set of linear
    equality and inequality constraints (hence to lie in a convex polytope
    that is a subset of the unit simplex).
	"""
	
	cran = "polyapost" 

	version("1.7", md5="b03e91ccfe7a5940ad115374c7d387a0")

	depends_on("r@3.6.2:", type=("build", "run"))
	depends_on("r-rcdd@1.2:", type=("build", "run"))
	depends_on("r-boot", type=("build", "run"))
