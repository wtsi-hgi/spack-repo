# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCallr(RPackage):
	"""Call R from R.

	It is sometimes useful to perform a computation in a separate R process,
	without affecting the current R process at all. This packages does exactly
	that."""

	cran = "callr"

	license("MIT")

	version("3.7.5", md5="fde3ee8095a576b253627bfe840ad133")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-processx@3.6.1:", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
