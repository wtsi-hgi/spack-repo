# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQuadroot(RPackage):
	"""Quadratic Root for any Quadratic Equation

	It will assist the user to find simple quadratic roots from any quadratic equation.
	"""
	
	cran = "QuadRoot" 

	version("0.2.1", md5="481f39ac63a3a1d869e7981ce3273e3c")

