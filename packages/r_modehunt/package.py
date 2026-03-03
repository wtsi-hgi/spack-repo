# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RModehunt(RPackage):
	"""Multiscale Analysis for Density Functions

	Given independent and identically distributed observations X(1), ..., X(n) from a density f,
 provides five methods to perform a multiscale analysis about f as well as the necessary critical
 values. The first method, introduced in Duembgen and Walther (2008), provides simultaneous confidence statements
 for the existence and location of local increases (or decreases) of f, based on all intervals I(all) spanned by
 any two observations X(j), X(k). The second method approximates the latter approach by using only a subset of
 I(all) and is therefore computationally much more efficient, but asymptotically equivalent. Omitting the additive
 correction term Gamma in either method offers another two approaches which are more powerful on small scales and
 less powerful on large scales, however, not asymptotically minimax optimal anymore. Finally, the block procedure is a
 compromise between adding Gamma or not, having intermediate power properties. The latter is again asymptotically
 equivalent to the first and was introduced in Rufibach and Walther (2010).
	"""
	
	homepage = "http://www.kasparrufibach.ch"
	cran = "modehunt" 

	version("1.0.7", md5="8f1a56f26624dce67c7dfaf0f243ba1c")

