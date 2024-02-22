# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCovrna(RPackage):
	"""Multivariate Analysis of Transcriptomic Data

	This package provides the analysis methods fourthcorner and RLQ analysis for large-scale transcriptomic data.
	"""
	
	bioc = "covRNA" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/covRNA_1.28.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/covRNA/covRNA_1.28.0.tar.gz"]

	version("1.28.0", md5="dd8405538f8c54345579ee7d0d5dc63f")

	depends_on("r-ade4", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-genefilter", type=("build", "run"))
