# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSssimple(RPackage):
	"""State Space Models

	Simulate, solve state space models.
	"""
	
	cran = "SSsimple" 

	version("0.6.6", md5="c2ceba6191ad122c9269670d6a2bf9d4")

	depends_on("r-mvtnorm", type=("build", "run"))
