# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBayesfmri(RPackage):
	"""Spatial Bayesian Methods for Task Functional MRI Studies

	Performs a spatial Bayesian general linear model (GLM) for task 
    functional magnetic resonance imaging (fMRI) data on the cortical surface. 
    Additional models include group analysis and inference to detect thresholded
    areas of activation. Includes direct support for the 'CIFTI' neuroimaging 
    file format. For more information see A. F. Mejia, Y. R. Yue, D. Bolin, F. 
    Lindgren, M. A. Lindquist (2020) <doi:10.1080/01621459.2019.1611582> and D. 
    Spencer, Y. R. Yue, D. Bolin, S. Ryan, A. F. Mejia (2022) 
    <doi:10.1016/j.neuroimage.2022.118908>.
	"""
	
	homepage = "https://github.com/mandymejia/BayesfMRI"
	cran = "BayesfMRI" 

	version("0.3.11", md5="636e4e1a71dd861b9921b8b385c433dd")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-ciftitools@0.8:", type=("build", "run"))
	depends_on("r-excursions", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-fmritools", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
