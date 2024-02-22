# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRcppcnpy(RPackage):
	"""Read-Write Support for 'NumPy' Files via 'Rcpp'.

	The 'cnpy' library written by Carl Rogers provides read and write
	facilities for files created with (or for) the 'NumPy' extension for
	'Python'. Vectors and matrices of numeric types can be read or written to
	and from files as well as compressed files. Support for integer files is
	available if the package has been built with -std=c++11 which should be the
	default on all platforms since the release of R 3.3.0."""

	cran = "RcppCNPy"

	version("0.2.12", md5="ab31a9d446bb5df24bc8964be9a56d05")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("zlib", type=("build", "link", "run"))
