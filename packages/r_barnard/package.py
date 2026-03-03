# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBarnard(RPackage):
	"""Barnard's Unconditional Test

	Barnard's unconditional test for 2x2 contingency tables.
	"""
	
	homepage = "https://github.com/kerguler/Barnard"
	cran = "Barnard" 

	version("1.8", md5="d9e19d6abf70c2fea846f03ec26eef17")

