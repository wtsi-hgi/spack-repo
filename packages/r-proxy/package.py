# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RProxy(RPackage):
	"""Distance and Similarity Measures.

	Provides an extensible framework for the efficient calculation of auto- and
	cross-proximities, along with implementations of the most popular ones."""

	cran = "proxy"

	license("GPL-2.0-only")

	version("0.4-27", md5="3e202df039c271d439193557645a54ba")

	depends_on("r@3.4:", type=("build", "run"))
