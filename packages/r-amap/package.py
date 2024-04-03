# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
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

	version("0.8-18", sha256="7afbbdd681a201121374821b733c9000ca1046a2353ee386507604c2c759ec7e")
	version("0.8-17", sha256="6b8473d1d35a9cbc611661882c8f681162e8f913f911ccd51629200ae72289c6")
	version("0.8-16", sha256="d3775ad7f660581f7d2f070e426be95ae0d6743622943e6f5491988e5217d4e2")
	version("0.8-19", md5="0693299e20587073c234e7c4a0079f95")

	depends_on("r@3.6:", type=("build", "run"))
