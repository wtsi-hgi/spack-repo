# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROveseg(RPackage):
	"""OVESEG-test to detect tissue/cell-specific markers

	An R package for multiple-group comparison to detect tissue/cell-specific marker genes among subtypes. It provides functions to compute OVESEG-test statistics, derive component weights in the mixture null distribution model and estimate p-values from weightedly aggregated permutations. Obtained posterior probabilities of component null hypotheses can also portrait all kinds of upregulation patterns among subtypes.
	"""
	
	bioc = "OVESEG" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/OVESEG_1.18.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/OVESEG/OVESEG_1.18.0.tar.gz"]

    version("1.24.0", tag="RELEASE_3_21")
	version("1.18.0", sha256="406e7d01bf6e2e3aec87ba755e3abc8032b0d86b5eb518f598b9fc6d35e8ea82")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-fdrtool", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
