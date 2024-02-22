# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBlockmissingdata(RPackage):
	"""Integrating Multi-Source Block-Wise Missing Data in Model
Selection

	Model selection method with multiple block-wise imputation for block-wise missing data; see Xue, F., and Qu, A. (2021) <doi:10.1080/01621459.2020.1751176>.
	"""
	
	cran = "BlockMissingData" 

	version("0.1.0", md5="1a65645f69aae31c66353890e670fd40")

	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-glmnetcr", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-pryr", type=("build", "run"))
