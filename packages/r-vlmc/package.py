# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVlmc(RPackage):
	"""Variable Length Markov Chains ('VLMC') Models

	Functions, Classes & Methods for estimation, prediction, and
  simulation (bootstrap) of Variable Length Markov Chain ('VLMC') Models.
	"""
	
	cran = "VLMC" 

	version("1.4-3-1", md5="fb49d76c9b141bdce6bb13c1c14588a1")

	depends_on("r-mass", type=("build", "run"))
