# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIsopat(RPackage):
	"""Calculation of isotopic pattern for a given molecular formula

	The function calculates the isotopic pattern (fine
        structures) for a given chemical formula.
	"""
	
	cran = "isopat" 

	version("1.0", md5="d83b7c1cea03eb4dfd2d60664e62d656")

