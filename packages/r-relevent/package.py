# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRelevent(RPackage):
	"""Relational Event Models

	Tools to fit and simulate realizations from relational event models.
	"""
	
	cran = "relevent" 

	version("1.2-1", md5="2ee80cf53cb5c8a6873afa926d2c501a")

	depends_on("r-trust", type=("build", "run"))
	depends_on("r-sna@2:", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
