# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDnaseqtest(RPackage):
	"""Generating and Testing DNA Sequences

	Generates DNA sequences based on Markov model techniques for matched sequences. This can be generalized to several sequences. The sequences (taxa) are then arranged in an evolutionary tree (phylogenetic tree) depicting how taxa diverge from their common ancestors. This gives the tests and estimation methods for the parameters of different models. Standard phylogenetic methods assume stationarity, homogeneity and reversibility for the Markov processes, and  often impose further restrictions on the parameters.
	"""
	
	cran = "DNAseqtest" 

	version("1.0", md5="b5402e3814e615079187d67096c5e5e1")

