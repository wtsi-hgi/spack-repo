# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNetwork(RPackage):
	"""Classes for Relational Data.

	Tools to create and modify network objects. The network class can represent
	a range of relational data types, and supports arbitrary vertex/edge/graph
	attributes."""

	cran = "network"

	license("GPL-2.0-or-later")

	version("1.18.2", md5="2bfbe1c797cdf37cc77e15679c1bf1ed")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-statnet-common@4.5:", type=("build", "run"))
