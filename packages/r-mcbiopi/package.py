# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMcbiopi(RPackage):
	"""Matrix Computation Based Identification of Prime Implicants

	Computes the prime implicants or a minimal disjunctive normal form for a
  logic expression presented by a truth table or a logic tree. Has been particularly 
  developed for logic expressions resulting from a logic regression analysis, i.e.
  logic expressions typically consisting of up to 16 literals, where the prime implicants 
  are typically composed of a maximum of 4 or 5 literals.
	"""
	
	cran = "mcbiopi" 

	version("1.1.6", md5="c77adce837eafd4e4bd4a571bdf6fb7c")

