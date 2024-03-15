# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBiocparallel(RPackage):
	"""Bioconductor facilities for parallel evaluation.

	This package provides modified versions and novel implementation of
	functions for parallel evaluation, tailored to use with Bioconductor
	objects."""

	bioc = "BiocParallel"
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/BiocParallel_1.36.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/BiocParallel/BiocParallel_1.36.0.tar.gz"]

	version("1.36.0", md5="a6a331ac453920e713836ddd0de38e25")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-futile-logger", type=("build", "run"))
	depends_on("r-snow", type=("build", "run"))
	depends_on("r-codetools", type=("build", "run"))
	depends_on("r-bh", type=("build", "run"))
	depends_on("r-cpp11", type=("build", "run"))
