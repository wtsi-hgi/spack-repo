# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGcspikelite(RPackage):
	"""Spike-in data for GC/MS data and methods within flagme

	Spike-in data for GC/MS data and methods within flagme
	"""
	
	bioc = "gcspikelite"

	version("1.46.0", commit="434621abfab4bf7d16dbd62fc1572f1dcaac083a")
	version("1.40.0", commit="9a2fd3b2241aa87a7b0873f96cb6f7a82d1b0914")

	depends_on("r@2.5:", type=("build", "run"))

