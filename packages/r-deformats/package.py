# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDeformats(RPackage):
	"""Differential gene expression data formats converter

	Convert between different data formats used by differential gene expression analysis tools.
	"""
	
	homepage = "https://github.com/aoles/DEFormats"
	bioc = "DEFormats" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/DEFormats_1.30.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/DEFormats/DEFormats_1.30.0.tar.gz"]

	version("1.30.0", sha256="4eb81b570e74d367718570be2b24c097dab1589e1b52db07cf67ba6ae665138d")

	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-deseq2", type=("build", "run"))
	depends_on("r-edger@3.13.4:", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
