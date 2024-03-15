# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RJade(RPackage):
	"""Blind Source Separation Methods Based on Joint Diagonalization and Some
	BSS Performance Criteria.

	Cardoso's JADE algorithm as well as his functions for joint diagonalization
	are ported to R. Also several other blind source separation (BSS) methods,
	like AMUSE and SOBI, and some criteria for performance evaluation of BSS
	algorithms, are given. The package is described in Miettinen, Nordhausen
	and Taskinen (2017) <doi:10.18637/jss.v076.i02>."""

	cran = "JADE"

	version("2.0-4", md5="b56c6d4b5be6b9300436ecb3e386fc80")

	depends_on("r-clue", type=("build", "run"))
