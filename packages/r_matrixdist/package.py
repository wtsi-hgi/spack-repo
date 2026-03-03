# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMatrixdist(RPackage):
	"""Statistics for Matrix Distributions

	Tools for phase-type distributions including the following variants:
    continuous, discrete, multivariate, in-homogeneous, right-censored, and regression. 
    Methods for functional evaluation, simulation and estimation using the 
    expectation-maximization (EM) algorithm are provided for all models.
    The methods of this package are based on the following references.
    Asmussen, S., Nerman, O., & Olsson, M. (1996). Fitting phase-type distributions via the EM algorithm,
    Olsson, M. (1996). Estimation of phase-type distributions from censored data,
    Albrecher, H., & Bladt, M. (2019) <doi:10.1017/jpr.2019.60>,
    Albrecher, H., Bladt, M., & Yslas, J. (2022) <doi:10.1111/sjos.12505>,
    Albrecher, H., Bladt, M., Bladt, M., & Yslas, J. (2022) <doi:10.1016/j.insmatheco.2022.08.001>,
    Bladt, M., & Yslas, J. (2022) <doi:10.1080/03461238.2022.2097019>,
    Bladt, M. (2022) <doi:10.1017/asb.2021.40>,
    Bladt, M. (2023) <doi:10.1080/10920277.2023.2167833>,
    Albrecher, H., Bladt, M., & Mueller, A. (2023) <doi:10.1515/demo-2022-0153>,
    Bladt, M. & Yslas, J. (2023) <doi:10.1016/j.insmatheco.2023.02.008>.
	"""
	
	homepage = "https://github.com/martinbladt/matrixdist_1.0"
	cran = "matrixdist" 

	version("1.1.9", md5="b3f1929db18476f32af6172b770c4754")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-nnet", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
