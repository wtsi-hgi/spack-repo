# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMfpca(RPackage):
	"""Multivariate Functional Principal Component Analysis for Data
Observed on Different Dimensional Domains

	Calculate a multivariate functional principal component analysis
    for data observed on different dimensional domains. The estimation algorithm
    relies on univariate basis expansions for each element of the multivariate
    functional data  (Happ & Greven, 2018) <doi:10.1080/01621459.2016.1273115>. 
    Multivariate and univariate functional data objects are
    represented by S4 classes for this type of data implemented in the package
    'funData'. For more details on the general concepts of both packages and a case 
    study, see Happ-Kurz (2020) <doi:10.18637/jss.v093.i05>.
	"""
	
	homepage = "https://github.com/ClaraHapp/MFPCA"
	cran = "MFPCA" 

	version("1.3-10", md5="1f3124143d0e1a923d05f88522f664af")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-fundata@1.3.4:", type=("build", "run"))
	depends_on("r-abind", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-irlba", type=("build", "run"))
	depends_on("r-matrix@1.5.0:", type=("build", "run"))
	depends_on("r-mgcv@1.8.33:", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("fftw@3.3.4:", type=("build", "link", "run"))
