# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRppairwisedesign(RPackage):
	"""Resolvable partially pairwise balanced design and Space-filling
design via association scheme

	Using some association schemes to obtain a new series of resolvable partially pairwise balanced designs (RPPBD) and space-filling designs.
	"""
	
	cran = "RPPairwiseDesign" 

	version("1.0", md5="d5f161ff3423c25f86116a29963d529b")

