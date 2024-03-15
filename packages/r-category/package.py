# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCategory(RPackage):
	"""Category Analysis.

	A collection of tools for performing category (gene set enrichment)
	analysis."""

	bioc = "Category"
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Category_2.68.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/Category/Category_2.68.0.tar.gz"]

	version("2.68.0", md5="d84fb36419834bb84721436d7f956932")

	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-graph", type=("build", "run"))
	depends_on("r-rbgl", type=("build", "run"))
	depends_on("r-gseabase", type=("build", "run"))
	depends_on("r-genefilter", type=("build", "run"))
	depends_on("r-annotate", type=("build", "run"))
	depends_on("r-dbi", type=("build", "run"))
