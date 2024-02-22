# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RClue(RPackage):
	"""Cluster Ensembles."""

	cran = "clue"

	version("0.3-65", md5="ee836dd0f273667e53d2e2208e57a07d")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
