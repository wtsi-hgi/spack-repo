# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLatticeextra(RPackage):
	"""Extra Graphical Utilities Based on Lattice.

	Building on the infrastructure provided by the lattice package, this
	package provides several new high-level functions and methods, as well as
	additional utilities such as panel and axis annotation functions."""

	cran = "latticeExtra"

	version("0.6-30", md5="81d8786cc01105f5a4043036b5165ab0")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-png", type=("build", "run"))
	depends_on("r-jpeg", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-interp", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
