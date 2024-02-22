# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMapproj(RPackage):
	"""Map Projections.

	Converts latitude/longitude into projected coordinates."""

	cran = "mapproj"

	version("1.2.11", md5="df2ac0dd6e0cb2331f089c36041580f7")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-maps@2.3.0:", type=("build", "run"))
