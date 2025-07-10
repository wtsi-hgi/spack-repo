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
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/covRNA_1.28.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/covRNA/covRNA_1.28.0.tar.gz"]

	version("1.28.0", sha256="04f091c52bb51de5423f0934b5fb6dbd8647b9b9e18aaee4c48a3783225174e6")

	depends_on("r-ade4", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-genefilter", type=("build", "run"))
