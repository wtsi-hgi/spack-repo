# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMirnapath(RPackage):
	"""miRNApath: Pathway Enrichment for miRNA Expression Data

	This package provides pathway enrichment techniques for miRNA expression data. Specifically, the set of methods handles the many-to-many relationship between miRNAs and the multiple genes they are predicted to target (and thus affect.)  It also handles the gene-to-pathway relationships separately. Both steps are designed to preserve the additive effects of miRNAs on genes, many miRNAs affecting one gene, one miRNA affecting multiple genes, or many miRNAs affecting many genes.
	"""
	
	bioc = "miRNApath" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/miRNApath_1.62.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/miRNApath/miRNApath_1.62.0.tar.gz"]

	version("1.62.0", md5="94aad8a3b57b070cb5c559d9d1f14726")

	depends_on("r@2.7:", type=("build", "run"))
