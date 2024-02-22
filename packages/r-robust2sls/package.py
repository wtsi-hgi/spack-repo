# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRobust2sls(RPackage):
	"""Outlier Robust Two-Stage Least Squares Inference and Testing

	An implementation of easy tools for outlier robust inference in
    two-stage least squares (2SLS) models. The user specifies a reference 
    distribution against which observations are classified as outliers or not. 
    After removing the outliers, adjusted standard errors are automatically 
    provided. Furthermore, several statistical tests for the false outlier 
    detection rate can be calculated. The outlier removing algorithm can be 
    iterated a fixed number of times or until the procedure converges. The 
    algorithms and robust inference are described in more detail in Jiao (2019) 
    <https://drive.google.com/file/d/1qPxDJnLlzLqdk94X9wwVASptf1MPpI2w/view>.
	"""
	
	homepage = "https://github.com/jkurle/robust2sls"
	cran = "robust2sls" 

	version("0.2.2", md5="a78666f2749c130a716582f0dff90932")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-exactci", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-ivreg", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-mathjaxr", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
