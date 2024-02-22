# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RConvevol(RPackage):
	"""Analysis of Convergent Evolution.

	Quantifies and assesses the significance of convergent evolution using two
	different methods (and 5 different measures) as described in Stayton (2015)
	<doi:10.1111/evo.12729>. Also displays results in a phylomorphospace
	framework."""

	cran = "convevol"

	version("2.0.1", md5="83d23750400e7059c01f663961051df0")

	depends_on("r-mass", type=("build", "run"))
	depends_on("r-ape", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-geiger", type=("build", "run"))
	depends_on("r-phytools", type=("build", "run"))
