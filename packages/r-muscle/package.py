# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMuscle(RPackage):
	"""Multiple Sequence Alignment with MUSCLE

	MUSCLE performs multiple sequence alignments of nucleotide or amino acid sequences.
	"""
	
	homepage = "http://www.drive5.com/muscle/"
	bioc = "muscle"

	version("3.50.0", commit="165f68e45fd4c28e452867faab01491e11ce4b78")
	version("3.44.0", commit="bebb424785add0eb586cec9ad56a14031f5bcf86")

	depends_on("r-biostrings", type=("build", "run"))
