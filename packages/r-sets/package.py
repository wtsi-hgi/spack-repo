# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSets(RPackage):
	"""Sets, Generalized Sets, Customizable Sets and Intervals

	Data structures and basic operations for ordinary sets, generalizations such
	as fuzzy sets, multisets, and fuzzy multisets, customizable sets, and
	intervals."""

	cran = "sets"

	maintainers("jgaeb")

	license("GPL-2.0-only")

	version("1.0-25", md5="a312dd5cf3d7df308781508d57c298b0")

	depends_on("r@2.7:", type=("build", "run"))
