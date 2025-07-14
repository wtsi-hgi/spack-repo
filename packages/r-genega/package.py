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

	version("1.58.0", tag="RELEASE_3_21")
	version("1.52.0", sha256="6a46418d2431be590f6901a1226fb65508393df5623a58364738263e8347044d")

	depends_on("r-seqinr", type=("build", "run"))
	depends_on("r-hash", type=("build", "run"))
