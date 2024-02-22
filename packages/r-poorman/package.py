# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPoorman(RPackage):
	"""A Poor Man's Dependency Free Recreation of 'dplyr'.

	A replication of key functionality from 'dplyr' and the wider 'tidyverse'
	using only 'base'."""

	cran = "poorman"

	version("0.2.7", md5="4bbc26912e651669c58e9eab98856f0f")

	depends_on("r@3.3:", type=("build", "run"))
