# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMtsys(RPackage):
	"""Methods in Mahalanobis-Taguchi (MT) System

	Mahalanobis-Taguchi (MT) system is a collection of multivariate
    analysis methods developed for the field of quality engineering. MT system
    consists of two families depending on their purpose. One is a family of
    Mahalanobis-Taguchi (MT) methods (in the broad sense) for diagnosis (see
    Woodall, W. H., Koudelik, R., Tsui, K. L., Kim, S. B., Stoumbos, Z. G., and
    Carvounis, C. P. (2003) <doi:10.1198/004017002188618626>) and the other is a
    family of Taguchi (T) methods for forecasting (see Kawada, H., and Nagata, Y.
    (2015) <doi:10.17929/tqs.1.12>). The MT package contains three basic methods
    for the family of MT methods and one basic method for the family of T
    methods. The MT method (in the narrow sense), the Mahalanobis-Taguchi
    Adjoint (MTA) methods, and the Recognition-Taguchi (RT) method are for the
    MT method and the two-sided Taguchi (T1) method is for the family of T
    methods. In addition, the Ta and Tb methods, which are the improved versions
    of the T1 method, are included.
	"""
	
	homepage = "https://github.com/okayaa/MTSYS"
	cran = "MTSYS" 

	version("1.2.0", md5="7afb0e07ad694765919a6c93b3cb7b86")

	depends_on("r@2.10:", type=("build", "run"))
