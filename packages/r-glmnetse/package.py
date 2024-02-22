# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGlmnetse(RPackage):
	"""Add Nonparametric Bootstrap SE to 'glmnet' for Selected
Coefficients (No Shrinkage)

	Builds a LASSO, Ridge, or Elastic Net model with 'glmnet' or
    'cv.glmnet' with bootstrap inference statistics (SE, CI, and p-value)
    for selected coefficients with no shrinkage applied for them. Model
    performance can be evaluated on test data and an automated alpha
    selection is implemented for Elastic Net. Parallelized computation is
    used to speed up the process. The methods are described in Friedman et
    al. (2010) <doi:10.18637/jss.v033.i01> and Simon et al. (2011)
    <doi:10.18637/jss.v039.i05>.
	"""
	
	homepage = "https://github.com/sebastianbahr/glmnetSE"
	cran = "glmnetSE" 

	version("0.0.1", md5="3ca922e09cfaaf0ab955e78b0517d8e4")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-boot", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
