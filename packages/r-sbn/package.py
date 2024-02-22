# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSbn(RPackage):
	"""Generate Stochastic Branching Networks

	Generate Stochastic Branching Networks ('SBNs'). Used to model the branching structure of rivers.
	"""
	
	homepage = "https://flee598.github.io/SBN/"
	cran = "SBN" 

	version("1.0.0", md5="fb3956007e3fb66eee9e1e5e58399f82")

	depends_on("r-igraph", type=("build", "run"))
