# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGuess(RPackage):
	"""Adjust Estimates of Learning for Guessing

	Adjust Estimates of Learning for Guessing. The package provides 
    standard guessing correction, and a latent class model that leverages
    informative pre-post transitions. For details of the latent class model,
    see <http://gsood.com/research/papers/guess.pdf>.
	"""
	
	homepage = "http://github.com/soodoku/guess"
	cran = "guess" 

	version("0.1", md5="344cdeba60abbffa274f0c78a28a7bd4")

	depends_on("r@3.2.1:", type=("build", "run"))
	depends_on("r-rsolnp", type=("build", "run"))
