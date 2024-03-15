# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAdsplit(RPackage):
	"""Annotation-Driven Clustering.

	This package implements clustering of microarray gene expression
	profiles according to functional annotations. For each term genes are
	annotated to, splits into two subclasses are computed and a significance
	of the supporting gene set is determined."""

	bioc = "adSplit"
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/adSplit_1.72.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/adSplit/adSplit_1.72.0.tar.gz"]

	version("1.72.0", md5="4d50affb50e6f6a11d8c4e379b6116d8")

	depends_on("r@2.1:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-biobase@1.5.12:", type=("build", "run"))
	depends_on("r-cluster@1.9.1:", type=("build", "run"))
	depends_on("r-go-db@1.8.1:", type=("build", "run"))
	depends_on("r-keggrest@1.30.1:", type=("build", "run"))
	depends_on("r-multtest@1.6:", type=("build", "run"))
