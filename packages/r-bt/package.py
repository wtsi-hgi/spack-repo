# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBt(RPackage):
	"""(Adaptive) Boosting Trees Algorithm

	Performs (Adaptive) Boosting Trees for Poisson distributed response variables, using log-link function.
  The code approach is similar to the one used in 'gbm'/'gbm3'. Moreover, each tree in the expansion is built thanks to the 'rpart' package.
  This package is based on following books and articles
  Denuit, M., Hainaut, D., Trufin, J. (2019) <doi:10.1007/978-3-030-25820-7>
  Denuit, M., Hainaut, D., Trufin, J. (2019) <doi:10.1007/978-3-030-57556-4>
  Denuit, M., Hainaut, D., Trufin, J. (2019) <doi:10.1007/978-3-030-25827-6>
  Denuit, M., Hainaut, D., Trufin, J. (2022) <doi:10.1080/03461238.2022.2037016>
  Denuit, M., Huyghe, J., Trufin, J. (2022) <https://dial.uclouvain.be/pr/boreal/fr/object/boreal%3A244325/datastream/PDF_01/view>
  Denuit, M., Trufin, J., Verdebout, T. (2022) <https://dial.uclouvain.be/pr/boreal/fr/object/boreal%3A268577>.
	"""
	
	homepage = "https://github.com/GiregWillame/BT/"
	cran = "BT" 

	version("0.4", md5="f953fbb418adb56729afa24627244f92")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-rpart", type=("build", "run"))
	depends_on("r-statmod", type=("build", "run"))
