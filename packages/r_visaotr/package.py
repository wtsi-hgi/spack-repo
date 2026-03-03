# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVisaotr(RPackage):
	"""Valid Improved Sparsity A-Learning for Optimal Treatment
Decision

	Valid Improved Sparsity A-Learning (VISA) provides a new method for selecting important variables involved in optimal treatment regime from a multiply robust perspective. The VISA estimator achieves its success by borrowing the strengths of both model averaging (ARM, Yuhong Yang, 2001) <doi:10.1198/016214501753168262> and variable selection (PAL, Chengchun Shi, Ailin Fan, Rui Song and Wenbin Lu, 2018) <doi:10.1214/17-AOS1570>. The package is an implementation of Zishu Zhan and Jingxiao Zhang. (2022+).
	"""
	
	cran = "visaOTR" 

	version("0.1.0", md5="0e2ce84c3196a59d6b231bd68c1ff616")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rglpk", type=("build", "run"))
	depends_on("r-e1071", type=("build", "run"))
	depends_on("r-kernlab", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-mboost", type=("build", "run"))
	depends_on("r-randomforest", type=("build", "run"))
	depends_on("r-xgboost", type=("build", "run"))
