# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMeat(RPackage):
	"""Muscle Epigenetic Age Test

	This package estimates epigenetic age in skeletal muscle, using DNA methylation data generated with the Illumina Infinium technology (HM27, HM450 and HMEPIC).
	"""
	
	homepage = "https://github.com/sarah-voisin/MEAT"
	bioc = "MEAT" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/MEAT_1.14.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/MEAT/MEAT_1.14.0.tar.gz"]

	version("1.14.0", md5="ea3f3041f0bdfab3844cea85f8d28c9b")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-impute@1.58:", type=("build", "run"))
	depends_on("r-dynamictreecut@1.63:", type=("build", "run"))
	depends_on("r-glmnet@2:", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-rpmm@1.25:", type=("build", "run"))
	depends_on("r-minfi@1.30:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-watermelon", type=("build", "run"))
