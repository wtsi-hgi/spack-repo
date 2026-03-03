# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTsqn(RPackage):
	"""Applications of the Qn Estimator to Time Series (Univariate and
Multivariate)

	Time Series Qn is a package with applications of the Qn estimator of Rousseeuw and Croux (1993) <doi:10.1080/01621459.1993.10476408> to univariate and multivariate Time Series in time and frequency domains. More specifically, the robust estimation of autocorrelation or autocovariance matrix functions from Ma and Genton (2000, 2001) <doi:10.1111/1467-9892.00203>, <doi:10.1006/jmva.2000.1942> and Cotta (2017) <doi:10.13140/RG.2.2.14092.10883> are provided. The robust pseudo-periodogram of Molinares et. al. (2009) <doi:10.1016/j.jspi.2008.12.014> is also given. This packages also provides the M-estimator of the long-memory parameter d based on the robustification of the GPH estimator proposed by Reisen et al. (2017) <doi:10.1016/j.jspi.2017.02.008>. 
	"""
	
	cran = "tsqn" 

	version("1.0.0", md5="b9b30f76aae9a769cbc99c93ee6f76bb")

	depends_on("r@3.2.3:", type=("build", "run"))
	depends_on("r-robustbase", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-fracdiff", type=("build", "run"))
