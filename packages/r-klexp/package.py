# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKlexp(RPackage):
	"""Kernel_lasso Expansion

	Provides the function to calculate the kernel-lasso expansion, Z-score, and max-min-scale standardization.It can increase the dimension of existed dataset and remove abundant features by lasso. Z Dai, L Jiayi, T Gong, C Wang (2021) <doi:10.1088/1742-6596/1955/1/012047>.
	"""
	
	homepage = "https://github.com/Zongrui-Dai/Kernel-lasso-feature-expansion"
	cran = "KLexp" 

	version("1.0.0", md5="94ed8827748f96938e438af8741dc965")

	depends_on("r-glmnet@4.1.2:", type=("build", "run"))
