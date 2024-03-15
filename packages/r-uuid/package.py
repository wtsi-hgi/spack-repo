# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack.package import *


class RUuid(RPackage):
	"""Tools for Generating and Handling of UUIDs.

	Tools for generating and handling of UUIDs (Universally Unique
	Identifiers)."""

	cran = "uuid"

	license("MIT")

	version("1.2-0", md5="e2888f2648528022ab731b3683bb7ea6")

	depends_on("r@2.9:", type=("build", "run"))
