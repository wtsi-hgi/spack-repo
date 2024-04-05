# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRhdf5(RPackage):
	"""R Interface to HDF5.

	This package provides an interface between HDF5 and R. HDF5's main
	features are the ability to store and access very large and/or complex
	datasets and a wide variety of metadata on mass storage (disk) through a
	completely portable file format. The rhdf5 package is thus suited for
	the exchange of large and/or complex datasets between R and other
	software package, and for letting R applications work on datasets that
	are larger than the available RAM."""

	bioc = "rhdf5"
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/rhdf5_2.46.1.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/rhdf5/rhdf5_2.46.1.tar.gz"]
	version("2.46.1", md5="947e662fe5f427ed0cc839e8049b431e", url="https://www.bioconductor.org/packages/3.18/bioc/src/contrib/rhdf5_2.46.1.tar.gz")
	version("2.44.0", commit="0f6e367ca9e97c37c683cd0f97c06732a67146f0")
	version("2.42.0", commit="fa26027d57b5b6d1c297446d9bbed74d5710c5d2")
	version("2.40.0", commit="fb6c15a3199f3ffd746fb9a381d574d17fef45a2")
	version("2.38.0", commit="f6fdfa807f5cd5a4d11d4aa6ebfaa81c118b4c3f")
	version("2.34.0", commit="ec861b81fc6962e844bf56b7549ba565a7e4c69c")
	version("2.28.1", commit="e230fa34d6f3e97dd4e6065115675baf5e8213bb")
	version("2.26.2", commit="81e11258db493661a19cf83e142b690ecac4e6cf")
	version("2.24.0", commit="e926e8ce4e77082781afb943324a1e6745385b48")
	version("2.22.0", commit="4431bdc0a2bcbb8086ee08a0f2300129b808d1be")
	version("2.20.0", commit="37b5165325062728bbec9167f89f5f4b794f30bc")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-rhdf5lib", type=("build", "run"))
	depends_on("r-rhdf5filters", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("zlib", type=("build", "link", "run"))
