# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPsea(RPackage):
	"""Population-Specific Expression Analysis.

	Deconvolution of gene expression data by Population-Specific Expression Analysis (PSEA).
	"""
	
	bioc = "PSEA" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/PSEA_1.36.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/PSEA/PSEA_1.36.0.tar.gz"]

	version("1.36.0", sha256="5ee830e1b1f6b11afa00ee2394405c0a79d4ae69d3124fe622e7ff6b99eaf609")

	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
