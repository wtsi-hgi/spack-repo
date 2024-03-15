# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFastica(RPackage):
	"""FastICA Algorithms to Perform ICA and Projection Pursuit.

	Implementation of FastICA algorithm to perform Independent Component
	Analysis (ICA) and Projection Pursuit."""

	cran = "fastICA"

	version("1.2-4", md5="0cc1a6b1e7c27d7c410cdfb0f0cb9e5a")

	depends_on("r@4:", type=("build", "run"))
