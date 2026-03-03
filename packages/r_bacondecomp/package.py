# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBacondecomp(RPackage):
	"""Goodman-Bacon Decomposition

	Decomposition for differences-in-differences with variation in
    treatment timing from Goodman-Bacon (2018) <doi:10.3386/w25018>.
	"""
	
	cran = "bacondecomp" 

	version("0.1.1", md5="7c2dd31437ed04526fd7e7d4d9859275")

	depends_on("r@2.10:", type=("build", "run"))
