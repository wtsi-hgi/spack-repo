# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSigfuge(RPackage):
	"""SigFuge

	Algorithm for testing significance of clustering in RNA-seq data.
	"""
	
	bioc = "SigFuge" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/SigFuge_1.40.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/SigFuge/SigFuge_1.40.0.tar.gz"]

	version("1.40.0", md5="cb03ecb39c2df4b4f5e1b49f8ba5d594")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-matlab", type=("build", "run"))
	depends_on("r-reshape", type=("build", "run"))
	depends_on("r-sigclust", type=("build", "run"))
