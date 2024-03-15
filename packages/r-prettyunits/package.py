# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPrettyunits(RPackage):
	"""Pretty, Human Readable Formatting of Quantities.

	Pretty, human readable formatting of quantities. Time intervals: 1337000 ->
	15d 11h 23m 20s. Vague time intervals: 2674000 -> about a month ago. Bytes:
	1337 -> 1.34 kB."""

	cran = "prettyunits"

	license("MIT")

	version("1.2.0", md5="2e2db8105f214b80d3d4254b8aabb255")

	depends_on("r@2.10:", type=("build", "run"))
