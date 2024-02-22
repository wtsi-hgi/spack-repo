# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTopgo(RPackage):
	"""Enrichment Analysis for Gene Ontology.

	topGO package provides tools for testing GO terms while accounting for
	the topology of the GO graph. Different test statistics and different
	methods for eliminating local similarities and dependencies between GO
	terms can be implemented and applied."""

	bioc = "topGO"
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/topGO_2.54.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/topGO/topGO_2.54.0.tar.gz"]

	version("2.54.0", md5="62aeda25dfb89dfd466ddc749e52a422")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-biocgenerics@0.13.6:", type=("build", "run"))
	depends_on("r-graph@1.14:", type=("build", "run"))
	depends_on("r-biobase@2:", type=("build", "run"))
	depends_on("r-go-db@2.3:", type=("build", "run"))
	depends_on("r-annotationdbi@1.7.19:", type=("build", "run"))
	depends_on("r-sparsem@0.73:", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-dbi", type=("build", "run"))
