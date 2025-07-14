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

	version("1.20.0", commit="24062c09b043e540b6aee63c51275eecd654b174")
	version("1.14.0", commit="d898e4399b0e4454bec4517dc886c7d9802d5d65")

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
