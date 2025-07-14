# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RScfeaturefilter(RPackage):
	"""A correlation-based method for quality filtering of single-cell RNAseq data

	An R implementation of the correlation-based method developed in the Joshi laboratory to analyse and filter processed single-cell RNAseq data. It returns a filtered version of the data containing only genes expression values unaffected by systematic noise.
	"""
	
	bioc = "scFeatureFilter" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/scFeatureFilter_1.22.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/scFeatureFilter/scFeatureFilter_1.22.0.tar.gz"]

    version("1.28.0", tag="RELEASE_3_21")
	version("1.22.0", sha256="7ba7d725929e95f3c4e3b8e505b4308eff76ab06c325473c9cd32ad75daa094e")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-dplyr@0.7.3:", type=("build", "run"))
	depends_on("r-ggplot2@2.1:", type=("build", "run"))
	depends_on("r-magrittr@1.5:", type=("build", "run"))
	depends_on("r-rlang@0.1.2:", type=("build", "run"))
	depends_on("r-tibble@1.3.4:", type=("build", "run"))
