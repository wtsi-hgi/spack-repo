# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBsgenomeEcoliNcbi20080805(RPackage):
	"""Escherichia coli full genomes

	Escherichia coli full genomes for several strains as provided by NCBI on 2008/08/05 and stored in Biostrings objects.
	"""
	
	bioc = "BSgenome.Ecoli.NCBI.20080805" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/BSgenome.Ecoli.NCBI.20080805_1.3.1000.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/BSgenome.Ecoli.NCBI.20080805/BSgenome.Ecoli.NCBI.20080805_1.3.1000.tar.gz"]

	version("1.3.1000", md5="c653e9cbee3faeb6fd5759b7575f234d", url="https://www.bioconductor.org/packages/release/data/annotation/src/contrib/BSgenome.Ecoli.NCBI.20080805_1.3.1000.tar.gz")
	version("1.3.1000", md5="c653e9cbee3faeb6fd5759b7575f234d", url="https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/BSgenome.Ecoli.NCBI.20080805_1.3.1000.tar.gz")

	depends_on("r-bsgenome", type=("build", "run"))

