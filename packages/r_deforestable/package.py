# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDeforestable(RPackage):
	"""Classify RGB Images into Forest or Non-Forest

	Implements two out-of box classifiers presented in <doi:10.48550/arXiv.2112.01063> for 
    distinguishing forest and non-forest terrain images. Under these algorithms, there are 
    frequentist approaches: one parametric, using stable distributions, and another one- 
    non-parametric, using the squared Mahalanobis distance. The package also contains functions for 
    data handling and building of new classifiers as well as some test data set.  
	"""
	
	cran = "deforestable" 

	version("3.1.1", md5="92efcb8d2c245208d271ae9e1056b911")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-terra", type=("build", "run"))
	depends_on("r-jpeg", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-stableestim", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
	depends_on("gdal@2.2.3:", type=("build", "link", "run"))
	depends_on("geos@3.4.0:", type=("build", "link", "run"))
	depends_on("proj@4.9.3:", type=("build", "link", "run"))
	depends_on("sqlite@3:", type=("build", "link", "run"))
