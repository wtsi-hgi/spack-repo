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
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/muscle_3.44.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/muscle/muscle_3.44.0.tar.gz"]

	version("3.44.0", sha256="bd98b350ad010b727c8c993b5056db2b0aca3349dbf2452e3d8e9acce502b272")

	depends_on("r-biostrings", type=("build", "run"))
