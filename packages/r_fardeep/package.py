# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFardeep(RPackage):
	"""Fast and Robust Deconvolution of Tumor Infiltrating Lymphocyte
from Expression Profiles using Least Trimmed Squares

	Using the idea of least trimmed square, it could automatically detects and removes outliers from data before estimating the coefficients. It is a robust machine learning tool which can be applied to gene-expression deconvolution technique. Yuning Hao, Ming Yan, Blake R. Heath, Yu L. Lei and Yuying Xie (2019) <doi:10.1101/358366>.
	"""
	
	cran = "FARDEEP" 

	version("1.0.1", md5="07d83fa5b9f5a95b1ba08c3529162174")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-nnls@1.4:", type=("build", "run"))
	depends_on("r-preprocesscore", type=("build", "run"))
