# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLattice(RPackage):
	"""Trellis Graphics for R.

	A powerful and elegant high-level data visualization system inspired by
	Trellis graphics, with an emphasis on multivariate data. Lattice is
	sufficient for typical graphics needs, and is also flexible enough to
	handle most nonstandard requirements. See ?Lattice for an introduction."""

	cran = "lattice"

	license("GPL-2.0-or-later")

	version("0.22-5", md5="74b2dd0ab4402df2382834082fea72db")

	depends_on("r@4:", type=("build", "run"))
