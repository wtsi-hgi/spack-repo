# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMnonr(RPackage):
	"""A Generator of Multivariate Non-Normal Random Numbers

	A data generator of multivariate non-normal data in R. It combines two different methods to generate non-normal data, one with user-specified multivariate skewness and kurtosis (more details can be found in the paper: Qu, Liu, & Zhang, 2019 <doi:10.3758/s13428-019-01291-5>), and the other with the given marginal skewness and kurtosis. The latter one is the widely-used Vale and Maurelli's method. It also contains a function to calculate univariate and multivariate (Mardia's Test) skew and kurtosis.
	"""
	
	cran = "mnonr" 

	version("1.0.0", md5="16c42e515f0f702b32b3f197f080d54a")

	depends_on("r@3.1:", type=("build", "run"))
