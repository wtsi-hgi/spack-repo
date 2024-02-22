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
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/muscle_3.44.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/muscle/muscle_3.44.0.tar.gz"]

	version("3.44.0", md5="159745260e624c7aeb3d2e0deeef99ab")

	depends_on("r-biostrings", type=("build", "run"))
