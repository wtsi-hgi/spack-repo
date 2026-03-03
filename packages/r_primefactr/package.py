# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPrimefactr(RPackage):
	"""Use Prime Factorization for Computations

	Use Prime Factorization for simplifying computations,
    for instance for ratios of large factorials.
	"""
	
	homepage = "https://github.com/privefl/primefactr"
	cran = "primefactr" 

	version("0.1.1", md5="e7a545627c2b15fa34d95ee6713e5077")

	depends_on("r@3.2.3:", type=("build", "run"))
