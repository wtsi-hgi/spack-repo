# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTriplex(RPackage):
	"""Search and visualize intramolecular triplex-forming sequences in DNA

	This package provides functions for identification and visualization of potential intramolecular triplex patterns in DNA sequence. The main functionality is to detect the positions of subsequences capable of folding into an intramolecular triplex (H-DNA) in a much larger sequence. The potential H-DNA (triplexes) should be made of as many cannonical nucleotide triplets as possible. The package includes visualization showing the exact base-pairing in 1D, 2D or 3D.
	"""
	
	homepage = "http://www.fi.muni.cz/~lexa/triplex/"
	bioc = "triplex" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/triplex_1.42.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/triplex/triplex_1.42.0.tar.gz"]

	version("1.42.0", md5="c66a6990486e7a4873b256d08eff9933")

	depends_on("r@2.15:", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-xvector", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
