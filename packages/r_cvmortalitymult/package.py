# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCvmortalitymult(RPackage):
	"""Cross-Validation for Multi-Population Mortality Models

	Implementation of cross-validation method for testing the forecasting accuracy of several multi-population mortality models. The family of multi-population includes several multi-population mortality models proposed through the actuarial and demography literature. The package includes functions for fitting and forecast the mortality rates of several populations. Additionally, we include functions for testing the forecasting accuracy of different multi-population models.
  References.
  Atance, D., Debon, A., and Navarro, E. (2020) <doi:10.3390/math8091550>.
  Bergmeir, C. & Benitez, J.M. (2012) <doi:10.1016/j.ins.2011.12.028>.
  Debon, A., Montes, F., & Martinez-Ruiz, F. (2011) <doi:10.1007/s13385-011-0043-z>.
  Lee, R.D. & Carter, L.R. (1992) <doi:10.1080/01621459.1992.10475265>.
  Russolillo, M., Giordano, G., & Haberman, S. (2011) <doi:10.1080/03461231003611933>.
  Santolino, M. (2023) <doi:10.3390/risks11100170>.
	"""
	
	homepage = "https://github.com/davidAtance/CvmortalityMult"
	cran = "CvmortalityMult" 

	version("0.0.1", md5="d6ed3fbc5e17e6eb32914456968c6e3c")

	depends_on("r@3.50:", type=("build", "run"))
	depends_on("r-stmomo", type=("build", "run"))
	depends_on("r-forecast", type=("build", "run"))
	depends_on("r-gnm", type=("build", "run"))
	depends_on("r-tmap", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
