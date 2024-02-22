# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBeachmat(RPackage):
	"""Compiling Bioconductor to Handle Each Matrix Type.

	Provides a consistent C++ class interface for reading from and writing
	data to a variety of commonly used matrix types. Ordinary matrices and
	several sparse/dense Matrix classes are directly supported, third-party
	S4 classes may be supported by external linkage, while all other
	matrices are handled by DelayedArray block processing."""

	bioc = "beachmat"
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/beachmat_2.18.1.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/beachmat/beachmat_2.18.1.tar.gz"]

	version("2.18.1", md5="37b7abdc24627d4abb87fd0beb5b3930")

	depends_on("r-delayedarray@0.27.2:", type=("build", "run"))
	depends_on("r-sparsearray", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
