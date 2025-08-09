# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack.package import *


class RUuid(RPackage):
	"""Tools for Generating and Handling of UUIDs.

	Tools for generating and handling of UUIDs (Universally Unique
	Identifiers)."""

	cran = "uuid"
	version("1.2-0", sha256="73710a14f812e34e891795b8945ea213f15ebcaf00b464b0e4b3fa09cf222afd")
	version("1.1-0", sha256="e75b50ee7dc8c4c8e7083023e954ffd1c6a004431bf5e9094463e46aa760f42f")
	version("1.0-3", sha256="456e4633659f20242fd7cd585ad005a3e07265f1d1db383fca6794c8ac2c8346")
	version("0.1-4", sha256="98e0249dda17434bfa209c2058e9911e576963d4599be9f7ea946e664f8ca93e")
	version("0.1-2", sha256="dd71704dc336b0857981b92a75ed9877d4ca47780b1682def28839304cd3b1be")

	depends_on("r@2.9:", type=("build", "run"))
