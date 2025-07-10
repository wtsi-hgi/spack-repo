# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMbased(RPackage):
	"""Package containing functions for ASE analysis using Meta-analysis Based Allele-Specific Expression Detection

	The package implements MBASED algorithm for detecting allele-specific gene expression from RNA count data, where allele counts at individual loci (SNVs) are integrated into a gene-specific measure of ASE, and utilizes simulations to appropriately assess the statistical significance of observed ASE.
	"""
	
	bioc = "MBASED" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/MBASED_1.36.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/MBASED/MBASED_1.36.0.tar.gz"]

	version("1.36.0", sha256="1df50969cabc1825ebf43538b4db0b472bdb21f0f6d5b163fe7ef1f0d0bdb23d")

	depends_on("r-runit", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
