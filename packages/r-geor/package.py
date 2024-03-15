# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGeor(RPackage):
	"""Analysis of Geostatistical Data.

	Geostatistical analysis including variogram-based, likelihood-based and
	Bayesian methods. Software companion for Diggle and Ribeiro (2007)
	<doi:10.1007/978-0-387-48536-2>."""

	cran = "geoR"

	version("1.9-4", md5="4474eaf884bc95726590a2b90e612d8f")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
	depends_on("r-splancs", type=("build", "run"))
