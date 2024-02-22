# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpgs(RPackage):
	"""Statistical Patterns in Genomic Sequences

	A collection of statistical hypothesis tests and other 
	techniques for identifying certain spatial relationships/phenomena in 
	DNA sequences. In particular, it provides tests and graphical methods for determining 
	whether or not DNA sequences comply with Chargaff's second parity rule 
	or exhibit purine-pyrimidine parity. In addition, there are functions for 
	efficiently simulating discrete state space Markov chains and testing 
	arbitrary symbolic sequences of symbols for the presence of first-order 
	Markovianness.
	Also, it has functions for counting words/k-mers (and cylinder patterns) in 
	arbitrary symbolic sequences. Functions which take a DNA sequence as input 
	can handle sequences stored as SeqFastadna objects from the 'seqinr' package.
	"""
	
	cran = "spgs" 

	version("1.0-4", md5="302975cd79db2a6cfa3e354d472b443a")

	depends_on("r@3:", type=("build", "run"))
