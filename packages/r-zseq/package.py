# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RZseq(RPackage):
	"""Integer Sequence Generator

	Generates well-known integer sequences. 'gmp' package is adopted for computing with arbitrarily large numbers. Every function has hyperlink to its corresponding item in OEIS (The On-Line Encyclopedia of Integer Sequences) in the function help page. For interested readers, see Sloane and Plouffe (1995, ISBN:978-0125586306).
	"""
	
	cran = "Zseq" 

	version("0.2.1", md5="4e8fa0944d2614870d8d5db3774f98d8")

	depends_on("r-gmp", type=("build", "run"))
