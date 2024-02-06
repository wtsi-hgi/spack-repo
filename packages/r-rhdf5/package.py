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
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/rhdf5_2.46.1.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/rhdf5/rhdf5_2.46.1.tar.gz"]

	version("2.46.1", md5="947e662fe5f427ed0cc839e8049b431e", url="https://www.bioconductor.org/packages/release/bioc/src/contrib/rhdf5_2.46.1.tar.gz")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-rhdf5lib", type=("build", "run"))
	depends_on("r-rhdf5filters", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("zlib", type=("build", "link", "run"))
