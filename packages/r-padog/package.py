# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPadog(RPackage):
	"""Pathway Analysis with Down-weighting of Overlapping Genes (PADOG)

	This package implements a general purpose gene set analysis method called PADOG that downplays the importance of genes that apear often accross the sets of genes to be analyzed. The package provides also a benchmark for gene set analysis methods in terms of sensitivity and ranking using 24 public datasets from KEGGdzPathwaysGEO package.
	"""
	
	bioc = "PADOG" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/PADOG_1.44.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/PADOG/PADOG_1.44.0.tar.gz"]

	version("1.50.0", tag="RELEASE_3_21")
	version("1.44.0", sha256="c72876d6cb9ab80aedce60510f5a3d6b6e75dc31ca8d980c7b805657a650cc7b")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-keggdzpathwaysgeo", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-gsa", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-dorng", type=("build", "run"))
	depends_on("r-hgu133plus2-db", type=("build", "run"))
	depends_on("r-hgu133a-db", type=("build", "run"))
	depends_on("r-keggrest", type=("build", "run"))
	depends_on("r-nlme", type=("build", "run"))
