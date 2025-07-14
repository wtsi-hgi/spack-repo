# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBloodcancermultiomics2017(RPackage):
	""""Drug-perturbation-based stratification of blood cancer" by Dietrich S, Oles M, Lu J et al. - experimental data and complete analysis

	The package contains data of the Primary Blood Cancer Encyclopedia (PACE) project together with a complete executable transcript of the statistical analysis and reproduces figures presented in the paper "Drug-perturbation-based stratification of blood cancer" by Dietrich S, Oles M, Lu J et al., J. Clin. Invest. (2018) 128(1):427-445. doi:10.1172/JCI93801.
	"""
	
	bioc = "BloodCancerMultiOmics2017" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/BloodCancerMultiOmics2017_1.22.1.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/BloodCancerMultiOmics2017/BloodCancerMultiOmics2017_1.22.1.tar.gz"]

	version("1.28.0", tag="RELEASE_3_21")
	version("1.22.1", md5="fabac1780c0616a91881b574e61ee31c", url="https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/BloodCancerMultiOmics2017_1.22.1.tar.gz")
	version("1.22.0", md5="d2b2dcb147bf904df505fedca2d1ea9e", url="https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/BloodCancerMultiOmics2017_1.22.0.tar.gz")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-beeswarm", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-deseq2", type=("build", "run"))
	depends_on("r-devtools", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggdendro", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-gtable", type=("build", "run"))
	depends_on("r-ipflasso", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))

