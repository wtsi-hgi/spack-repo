# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAmap(RPackage):
	"""Another Multidimensional Analysis Package.

	Tools for Clustering and Principal Component Analysis (With robust methods,
	and parallelized functions)."""

	cran = "amap"

	license("GPL-2.0-or-later")

	version("0.8-19", md5="0693299e20587073c234e7c4a0079f95")

	depends_on("r@3.6:", type=("build", "run"))
