# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGseabase(RPackage):
	"""Gene set enrichment data structures and methods.

	This package provides classes and methods to support Gene Set Enrichment
	Analysis (GSEA)."""

	bioc = "GSEABase"
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/GSEABase_1.64.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/GSEABase/GSEABase_1.64.0.tar.gz"]

	version("1.64.0", md5="a9d4d48654c9a05cdec2f09f8f805c4e")

	depends_on("r@2.6:", type=("build", "run"))
	depends_on("r-biocgenerics@0.13.8:", type=("build", "run"))
	depends_on("r-biobase@2.17.8:", type=("build", "run"))
	depends_on("r-annotate@1.45.3:", type=("build", "run"))
	depends_on("r-graph@1.37.2:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-xml", type=("build", "run"))
