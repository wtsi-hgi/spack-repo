# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpatstatData(RPackage):
	"""Datasets for 'spatstat' Family.

	Contains all the datasets for the 'spatstat' family of packages."""

	cran = "spatstat.data"

	version("3.0-4", md5="21d5a23ffd441d3568230fc5bff15015")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-spatstat-utils@3.0.2:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
