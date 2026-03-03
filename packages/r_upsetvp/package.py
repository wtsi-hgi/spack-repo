# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RUpsetvp(RPackage):
	"""An Alternative Visualization of VPA and HP in Canonical Analysis

	Using matrix layout to visualize the unique, common, or individual contribution of each predictor (or matrix of predictors) towards explained variation on canonical analysis. These contributions were derived from variance partitioning analysis (VPA) and hierarchical partitioning (HP), applying the algorithm of Lai J., Zou Y., Zhang J., Peres-Neto P. (2022) Generalizing hierarchical and variation partitioning in multiple regression and canonical analyses using the rdacca.hp R package.Methods in Ecology and Evolution, 13: 782-788 <doi:10.1111/2041-210X.13800>.
	"""
	
	homepage = "https://github.com/LiuXYh/UpSetVP"
	cran = "UpSetVP" 

	version("1.0.0", md5="0065adfc855d86d72601611fd6b770f4")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-rdacca-hp", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-patchwork", type=("build", "run"))
