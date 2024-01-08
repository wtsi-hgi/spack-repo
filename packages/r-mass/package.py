# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMass(RPackage):
	"""Support Functions and Datasets for Venables and Ripley's MASS.

	Functions and datasets to support Venables and Ripley, "Modern Applied
	Statistics with S" (4th edition, 2002)."""

	cran = "MASS"

	version("7.3-60", md5="24ac97ba3e4446708f9bb9b8911eb920")

	depends_on("r@4.0:", type=("build", "run"))
