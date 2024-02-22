# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMpsem(RPackage):
	"""Modeling Phylogenetic Signals using Eigenvector Maps

	Computational tools to represent phylogenetic signals using adapted eigenvector maps.
	"""
	
	cran = "MPSEM" 

	version("0.4-1", md5="d5b3af207a2c1547f62e72a44539dc34")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-ape", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
