# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSlimrec(RPackage):
	"""Sparse Linear Method to Predict Ratings and Top-N
Recommendations

	Sparse Linear Method(SLIM) predicts ratings and top-n
    recommendations suited for sparse implicit positive feedback systems. SLIM
    is decomposed into multiple elasticnet optimization problems which are solved
    in parallel over multiple cores. The package is based on "SLIM: Sparse Linear
    Methods for Top-N Recommender Systems" by Xia Ning and George Karypis <doi:10.1109/ICDM.2011.134>.
	"""
	
	cran = "slimrec" 

	version("0.1.0", md5="5c46b62db9904c4cf28ed4d937da962e")

	depends_on("r@3.3.3:", type=("build", "run"))
	depends_on("r-assertthat@0.1:", type=("build", "run"))
	depends_on("r-matrix@1.2.8:", type=("build", "run"))
	depends_on("r-glmnet@2.0.5:", type=("build", "run"))
	depends_on("r-bigmemory@4.5.19:", type=("build", "run"))
	depends_on("r-pbapply@1.3.2:", type=("build", "run"))
