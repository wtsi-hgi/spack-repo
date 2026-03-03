# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGenega(RPackage):
	"""Design gene based on both mRNA secondary structure and codon usage bias using Genetic algorithm

	R based Genetic algorithm for gene expression optimization by considering both mRNA secondary structure and codon usage bias, GeneGA includes the information of highly expressed genes of almost 200 genomes. Meanwhile, Vienna RNA Package is needed to ensure GeneGA to function properly.
	"""
	
	homepage = "http://www.tbi.univie.ac.at/~ivo/RNA/"
	bioc = "GeneGA" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/GeneGA_1.52.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/GeneGA/GeneGA_1.52.0.tar.gz"]

	version("1.52.0", md5="3047f864af1845ce91869fc2560733c4")

	depends_on("r-seqinr", type=("build", "run"))
	depends_on("r-hash", type=("build", "run"))
