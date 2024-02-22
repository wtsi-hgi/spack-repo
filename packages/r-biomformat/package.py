# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBiomformat(RPackage):
	"""An interface package for the BIOM file format.

	This is an R package for interfacing with the BIOM format. This package
	includes basic tools for reading biom-format files, accessing and
	subsetting data tables from a biom object (which is more complex than a
	single table), as well as limited support for writing a biom-object back
	to a biom-format file. The design of this API is intended to match the
	python API and other tools included with the biom-format project, but
	with a decidedly "R flavor" that should be familiar to R users. This
	includes S4 classes and methods, as well as extensions of common core
	functions/methods."""

	bioc = "biomformat"
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/biomformat_1.30.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/biomformat/biomformat_1.30.0.tar.gz"]

	version("1.30.0", md5="f35aaf72b454bc1872f1247642029006")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-plyr@1.8:", type=("build", "run"))
	depends_on("r-jsonlite@0.9.16:", type=("build", "run"))
	depends_on("r-matrix@1.2:", type=("build", "run"))
	depends_on("r-rhdf5", type=("build", "run"))
