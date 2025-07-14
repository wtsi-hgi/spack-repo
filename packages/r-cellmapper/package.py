# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCellmapper(RPackage):
	"""Predict genes expressed selectively in specific cell types

	Infers cell type-specific expression based on co-expression similarity with known cell type marker genes. Can make accurate predictions using publicly available expression data, even when a cell type has not been isolated before.
	"""
	
	bioc = "CellMapper" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/CellMapper_1.28.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/CellMapper/CellMapper_1.28.0.tar.gz"]

    version("1.34.0", tag="RELEASE_3_21")
	version("1.28.0", sha256="9bef07abde4a48a08e40991c52cb98a6e55d3cbb79fcdf20b1bb60c5019f49e5")

	depends_on("r-s4vectors", type=("build", "run"))
