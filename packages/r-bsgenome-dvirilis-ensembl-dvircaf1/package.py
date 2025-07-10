# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBsgenomeDvirilisEnsemblDvircaf1(RPackage):
	"""Full genome sequences for Drosophila virilis (assembly dvir_caf1)

	Full genome sequences for Drosophila virilis (assembly dvir_caf1, GenBank assembly accession GCA_000005245.1) as provided by Ensembl and stored in Biostrings objects.
	"""
	
	bioc = "BSgenome.Dvirilis.Ensembl.dvircaf1" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/BSgenome.Dvirilis.Ensembl.dvircaf1_1.4.3.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/BSgenome.Dvirilis.Ensembl.dvircaf1/BSgenome.Dvirilis.Ensembl.dvircaf1_1.4.3.tar.gz"]

	version("1.4.3", sha256="15ed0f5e749078d0cf49b17029b6d178dfcf846170943e6e9aa9d6d12fd49837", url="https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/BSgenome.Dvirilis.Ensembl.dvircaf1_1.4.3.tar.gz")

	depends_on("r-bsgenome", type=("build", "run"))

