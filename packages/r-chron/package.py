# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RChron(RPackage):
	"""Chronological objects which can handle dates and times.

	Provides chronological objects which can handle dates and times."""

	cran = "chron"

	version("2.3-61", md5="5eaa5b818bc0f0dd7eeba9478bd9da88")

	depends_on("r@2.12:", type=("build", "run"))
