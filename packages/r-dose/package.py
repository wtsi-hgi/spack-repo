# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDose(RPackage):
	"""Disease Ontology Semantic and Enrichment analysis.

	This package implements five methods proposed by Resnik, Schlicker,
	Jiang, Lin and Wang respectively for measuring semantic similarities
	among DO terms and gene products. Enrichment analyses including
	hypergeometric model and gene set enrichment analysis are also
	implemented for discovering disease associations of high-throughput
	biological data."""

	bioc = "DOSE"
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/DOSE_3.28.2.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/DOSE/DOSE_3.28.2.tar.gz"]

	version("3.28.2", md5="db9c95935ce192a915b1246380f625d5")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-hdo-db", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-fgsea", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-gosemsim@2.27.1:", type=("build", "run"))
	depends_on("r-qvalue", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-yulab-utils", type=("build", "run"))
