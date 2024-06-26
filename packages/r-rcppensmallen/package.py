# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRcppensmallen(RPackage):
	"""Rcpp integration for the Ensmallen templated C++ mathematical	optimization library."""

	cran = "RcppEnsmallen"
	version("0.2.21.1.1", md5="6c3bf63aae39e2147d24f0af052c5a1e")
	version( "0.2.19.0.1", sha256="b4a9bde4dde309a52a47b56790389ecab14fe64066098d2a38b1b588ba3d8631")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo@0.9.800:", type=("build", "run"))
