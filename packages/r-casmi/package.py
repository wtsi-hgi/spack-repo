# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCasmi(RPackage):
	"""'CASMI'-Based Functions

	Contains Coverage Adjusted Standardized Mutual Information ('CASMI')-based functions. 'CASMI' is a fundamental concept of a series of methods. For more information about 'CASMI' and 'CASMI'-related methods, please refer to the corresponding publications (e.g., a feature selection method, Shi, J., Zhang, J., & Ge, Y. (2019) <doi:10.3390/e21121179>, and a dataset quality measurement method, Shi, J., Zhang, J., & Ge, Y. (2019) <doi:10.1109/ICHI.2019.8904553>) or contact the package author for the latest updates.
	"""
	
	cran = "CASMI" 

	version("1.2.2", md5="e275b1c66fbb78b75ff60cbd9a97e6a8")

	depends_on("r-entropyestimation", type=("build", "run"))
	depends_on("r-entropy", type=("build", "run"))
