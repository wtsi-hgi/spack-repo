# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCancersubtypes(RPackage):
	"""Cancer subtypes identification, validation and visualization based on multiple genomic data sets

	CancerSubtypes integrates the current common computational biology methods for cancer subtypes identification and provides a standardized framework for cancer subtype analysis based multi-omics data, such as gene expression, miRNA expression, DNA methylation and others.
	"""
	
	homepage = "https://github.com/taoshengxu/CancerSubtypes"
	bioc = "CancerSubtypes" 

	version("1.28.0", commit="03e787be5adcf0cdcc3a3cc3fffc71774a73bda8")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-sigclust", type=("build", "run"))
	depends_on("r-nmf", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-impute", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-consensusclusterplus", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
