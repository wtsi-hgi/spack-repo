# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRtsne(RPackage):
	"""T-Distributed Stochastic Neighbor Embedding using a Barnes-Hut
	Implementation.

	An R wrapper around the fast T-distributed Stochastic Neighbor Embedding
	implementation."""

	cran = "Rtsne"

	version("0.17", md5="06863d3c06a170d03d3600d78a80052a")

	depends_on("r-rcpp", type=("build", "run"))
