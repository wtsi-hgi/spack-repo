# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RClinsig(RPackage):
	"""Clinical Significance Functions

	Functions for calculating clinical significance.
	"""
	
	cran = "clinsig" 

	version("1.2", md5="4e8da6ee9ecc8c7384da310be585cf4f")

