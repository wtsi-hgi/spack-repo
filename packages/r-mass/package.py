# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMass(RPackage):
	"""Support Functions and Datasets for Venables and Ripley's MASS.

	Functions and datasets to support Venables and Ripley, "Modern Applied
	Statistics with S" (4th edition, 2002)."""

	cran = "MASS"

	version("7.3-60.0.1", md5="a6cf0337e79798901d57410c704abc82")

	depends_on("r@4:", type=("build", "run"))
