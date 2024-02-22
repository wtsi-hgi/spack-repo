# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPbapply(RPackage):
	"""Adding Progress Bar to '*apply' Functions.

	A lightweight package that adds progress bar to vectorized R functions
	('*apply'). The implementation can easily be added to functions where
	showing the progress is useful (e.g. bootstrap). The type and style of the
	progress bar (with percentages or remaining time) can be set through
	options. Supports several parallel processing backends."""

	cran = "pbapply"

	version("1.7-2", md5="76c7702f9ffb732731c431ee4b6fdfb2")

	depends_on("r@3.2:", type=("build", "run"))
