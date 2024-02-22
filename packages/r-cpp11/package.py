# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCpp11(RPackage):
	"""A C++11 Interface for R's C Interface.

	Provides a header only, C++11 interface to R's C interface. Compared to
	other approaches 'cpp11' strives to be safe against long jumps from the C
	API as well as C++ exceptions, conform to normal R function semantics and
	supports interaction with 'ALTREP' vectors."""

	cran = "cpp11"

	version("0.4.7", md5="3e1399c740f88a8a76cc6c688dcc9337", url="https://cran.r-project.org/src/contrib/cpp11_0.4.7.tar.gz")

	depends_on("r@3.5:", type=("build", "run"))
