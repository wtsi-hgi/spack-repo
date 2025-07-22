# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RArrmnormalization(RPackage):
	"""Adaptive Robust Regression normalization for Illumina methylation data

	Perform the Adaptive Robust Regression method (ARRm) for the normalization of methylation data from the Illumina Infinium HumanMethylation 450k assay.
	"""
	
	bioc = "ARRmNormalization" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/ARRmNormalization_1.42.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/ARRmNormalization/ARRmNormalization_1.42.0.tar.gz"]

	version("1.42.0", sha256="5572e2a5fccb6da841b8dd7516403da5c74891772bee6bc5040bbf27b8bba1b9")

	depends_on("r@2.15.1:", type=("build", "run"))
	depends_on("r-arrmdata", type=("build", "run"))
