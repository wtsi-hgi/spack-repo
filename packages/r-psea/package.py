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
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/PSEA_1.36.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/PSEA/PSEA_1.36.0.tar.gz"]

	version("1.36.0", md5="c8f9f8210c265d722d76668e19a6fd7c")

	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
