# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCometexacttest(RPackage):
	"""Exact Test from the Combinations of Mutually Exclusive
Alterations (CoMEt) Algorithm

	An algorithm for identifying combinations of mutually exclusive alterations in cancer genomes. CoMEt represents the mutations in a set M of k genes with a 2^k dimensional contingency table, and then computes the tail probability of observing T(M) exclusive alterations using an exact statistical test.
	"""
	
	homepage = "http://compbio.cs.brown.edu/projects/comet"
	cran = "cometExactTest" 

	version("0.1.5", md5="c2a0ab7312a81a1f53e5d7c0f0cc80c6")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
