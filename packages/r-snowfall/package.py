# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSnowfall(RPackage):
	"""Easier cluster computing (based on snow).

	Usability wrapper around snow for easier development of parallel R
	programs. This package offers e.g. extended error checks, and additional
	functions. All functions work in sequential mode, too, if no cluster is
	present or wished. Package is also designed as connector to the cluster
	management tool sfCluster, but can also used without it."""

	cran = "snowfall"

	license("GPL-2.0-or-later")

	version("1.84-6.3", md5="4ca758a26dd4e862cc9ffd43ae16b2d3")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-snow", type=("build", "run"))
