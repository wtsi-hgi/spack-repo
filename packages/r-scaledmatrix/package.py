# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RScaledmatrix(RPackage):
	"""Creating a DelayedMatrix of Scaled and Centered Values.

	Provides delayed computation of a matrix of scaled and centered values.
	The result is equivalent to using the scale() function but avoids explicit
	realization of a dense matrix during block processing. This permits greater
	efficiency in common operations, most notably matrix multiplication."""

	bioc = "ScaledMatrix"
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/ScaledMatrix_1.10.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/ScaledMatrix/ScaledMatrix_1.10.0.tar.gz"]

	version("1.10.0", md5="337f2af494241ac5def9fcae4dc12313")

	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-delayedarray", type=("build", "run"))
