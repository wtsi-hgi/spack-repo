# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBorealis(RPackage):
	"""Bisulfite-seq OutlieR mEthylation At singLe-sIte reSolution

	Borealis is an R library performing outlier analysis for count-based bisulfite sequencing data. It detectes outlier methylated CpG sites from bisulfite sequencing (BS-seq). The core of Borealis is modeling Beta-Binomial distributions. This can be useful for rare disease diagnoses.
	"""
	
	bioc = "borealis" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/borealis_1.6.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/borealis/borealis_1.6.0.tar.gz"]

    version("1.12.0", tag="RELEASE_3_21")
	version("1.6.0", sha256="44a51762bb980824db6979645d2ade9cb7e2947382e276af5752fb715a766290")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-snow", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-gamlss", type=("build", "run"))
	depends_on("r-gamlss-dist", type=("build", "run"))
	depends_on("r-bsseq", type=("build", "run"))
	depends_on("r-dss", type=("build", "run"))
	depends_on("r-r-utils", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-cowplot", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
