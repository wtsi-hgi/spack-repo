# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFitheavytail(RPackage):
	"""Mean and Covariance Matrix Estimation under Heavy Tails

	Robust estimation methods for the mean vector, scatter matrix,
    and covariance matrix (if it exists) from data (possibly containing NAs) 
    under multivariate heavy-tailed distributions such as angular Gaussian 
    (via Tyler's method), Cauchy, and Student's t distributions. Additionally, 
    a factor model structure can be specified for the covariance matrix. The
    latest revision also includes the multivariate skewed t distribution.
    The package is based on the papers: Sun, Babu, and Palomar (2014);
    Sun, Babu, and Palomar (2015); Liu and Rubin (1995);
    Zhou, Liu, Kumar, and Palomar (2019); Pascal, Ollila, and Palomar (2021).
	"""
	
	homepage = "https://CRAN.R-project.org/package=fitHeavyTail"
	cran = "fitHeavyTail" 

	version("0.2.0", md5="e3e76a54d74f7438213b39e9156a0722")

	depends_on("r-icsnp", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-ghyp", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
