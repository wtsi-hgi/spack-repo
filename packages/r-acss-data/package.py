# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAcssData(RPackage):
	"""Data Only: Algorithmic Complexity of Short Strings (Computed via
Coding Theorem Method)

	Data only package providing the algorithmic complexity of short strings, computed using the coding theorem method. For a given set of symbols in a string, all possible or a large number of random samples of Turing machines (TM) with a given number of states (e.g., 5) and number of symbols corresponding to the number of symbols in the strings were simulated until they reached a halting state or failed to end. This package contains data on 4.5 million strings from length 1 to 12 simulated on TMs with 2, 4, 5, 6, and 9 symbols. The complexity of the string corresponds to the distribution of the halting states of the TMs.
	"""
	
	homepage = "http://complexitycalculator.com/methodology.html"
	cran = "acss.data" 

	version("1.0", md5="c4693bbadf6fbb2e1376fef336277614")

	depends_on("r@2.10:", type=("build", "run"))
