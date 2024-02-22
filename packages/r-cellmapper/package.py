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
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/CellMapper_1.28.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/CellMapper/CellMapper_1.28.0.tar.gz"]

	version("1.28.0", md5="ca94af55dbc55bb2bf40c69f4965b553")

	depends_on("r-s4vectors", type=("build", "run"))
