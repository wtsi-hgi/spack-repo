# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQsvar(RPackage):
	"""Generate Quality Surrogate Variable Analysis for Degradation Correction

	The qsvaR package contains functions for removing the effect of degration in rna-seq data from postmortem brain tissue. The package is equipped to help users generate principal components associated with degradation. The components can be used in differential expression analysis to remove the effects of degradation.
	"""
	
	homepage = "https://github.com/LieberInstitute/qsvaR"
	bioc = "qsvaR" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/qsvaR_1.6.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/qsvaR/qsvaR_1.6.0.tar.gz"]

	version("1.12.0", tag="RELEASE_3_21")
	version("1.6.0", sha256="4cf3c4b26e421aed9f6c536fbe48cc21ea14d887311f3a4c46a58e38b94201d8")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-sva", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
