# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSimplifyenrichment(RPackage):
	"""Simplify Functional Enrichment Results

	A new clustering algorithm, "binary cut", for clustering similarity matrices of functional terms is implemeted in this package. It also provides functions for visualizing, summarizing and comparing the clusterings.
	"""
	
	homepage = "https://github.com/jokergoo/simplifyEnrichment"
	bioc = "simplifyEnrichment" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/simplifyEnrichment_1.12.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/simplifyEnrichment/simplifyEnrichment_1.12.0.tar.gz"]

	version("1.12.0", md5="d54c7188ca88dd43802296650e5b80e1")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-gosemsim", type=("build", "run"))
	depends_on("r-complexheatmap@2.7.4:", type=("build", "run"))
	depends_on("r-circlize", type=("build", "run"))
	depends_on("r-getoptlong", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
	depends_on("r-tm", type=("build", "run"))
	depends_on("r-go-db", type=("build", "run"))
	depends_on("r-org-hs-eg-db", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-slam", type=("build", "run"))
	depends_on("r-clue", type=("build", "run"))
	depends_on("r-proxyc", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-cluster@1.14.2:", type=("build", "run"))
	depends_on("r-colorspace", type=("build", "run"))
	depends_on("r-globaloptions@0.1:", type=("build", "run"))
