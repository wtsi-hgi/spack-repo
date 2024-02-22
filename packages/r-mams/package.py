# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMams(RPackage):
	"""Designing Multi-Arm Multi-Stage Studies

	Designing multi-arm multi-stage studies with (asymptotically) normal endpoints and known variance.
	"""
	
	cran = "MAMS" 

	version("2.0.1", md5="06f0736b2f1d8cd5188d5584ed1a6469")

	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-future", type=("build", "run"))
	depends_on("r-future-apply", type=("build", "run"))
