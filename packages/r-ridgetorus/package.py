# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRidgetorus(RPackage):
	"""PCA on the Torus via Density Ridges

	Implementation of a Principal Component Analysis (PCA) in the
    torus via density ridge estimation. The main function, ridge_pca(), obtains
    the relevant density ridge for bivariate sine von Mises and bivariate
    wrapped Cauchy distribution models and provides the associated scores and
    variance decomposition. Auxiliary functions for evaluating, fitting, and
    sampling these models are also provided. The package provides replicability
    to García-Portugués and Prieto-Tirado (2023) 
    <doi:10.1007/s11222-023-10273-9>.
	"""
	
	homepage = "https://github.com/egarpor/ridgetorus"
	cran = "ridgetorus" 

	version("1.0.2", md5="99479608b684ab23bc5e6c555a0f8d8a")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rootsolve", type=("build", "run"))
	depends_on("r-sdetorus", type=("build", "run"))
	depends_on("r-sphunif", type=("build", "run"))
	depends_on("r-circular", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
