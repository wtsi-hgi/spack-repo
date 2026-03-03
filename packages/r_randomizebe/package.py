# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRandomizebe(RPackage):
	"""Create a Random List for Crossover Studies

	Contains a function to randomize subjects, patients in groups of 
   sequences (treatment sequences).
   If a blocksize is given, the randomization will be done within blocks.
   The randomization may be controlled by a Wald-Wolfowitz runs test.
   Functions to obtain the p-value of that test are included.
   The package is mainly intended for randomization of bioequivalence studies
   but may be used also for other clinical crossover studies.
   Contains two helper functions sequences() and williams() to get the sequences 
   of commonly used designs in BE studies.
	"""
	
	cran = "randomizeBE" 

	version("0.3-6", md5="86753f5dcd8d0498d44fbb19a32a5353")

