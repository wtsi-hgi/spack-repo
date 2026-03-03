# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRtrng(RPackage):
	"""Advanced and Parallel Random Number Generation via 'TRNG'

	Embeds sources and headers from Tina's Random
    Number Generator ('TRNG') C++ library. Exposes some functionality for
    easier access, testing and benchmarking into R. Provides examples of
    how to use parallel RNG with 'RcppParallel'. The methods and
    techniques behind 'TRNG' are illustrated in the package vignettes and
    examples. Full documentation is available in Bauke (2021)
    <https://github.com/rabauke/trng4/blob/v4.23.1/doc/trng.pdf>.
	"""
	
	homepage = "https://github.com/miraisolutions/rTRNG#readme"
	cran = "rTRNG" 

	version("4.23.1-2", md5="b53d8c4475b17d5ff3189ca36be98214")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcppparallel", type=("build", "run"))
