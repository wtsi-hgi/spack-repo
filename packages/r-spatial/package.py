# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpatial(RPackage):
	"""Functions for Kriging and Point Pattern Analysis.

	Functions for kriging and point pattern analysis."""

	cran = "spatial"

	version("7.3-17", md5="75ae4757dcf945ca276634c716393c1b")

	depends_on("r@3:", type=("build", "run"))
