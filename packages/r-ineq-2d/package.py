# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIneq2d(RPackage):
	"""Two-Dimensional Decomposition of the Theil Index and the Squared
Coefficient of Variation

	Decomposition of income inequality by groups formed of individuals 
    possessing similar characteristics (e.g., sex, education, age) and their 
    income sources at the same time.
    Decomposition of the Theil index is based on Giammatteo, M. (2007) 
    <https://www.lisdatacenter.org/wps/liswps/466.pdf>.
    Decomposition of the squared coefficient of variation is based on
    Garcia-Penalosa, C., & Orgiazzi, E. (2013) <doi:10.1111/roiw.12054>.
	"""
	
	homepage = "https://github.com/sklivan/ineq.2d"
	cran = "ineq.2d" 

	version("0.1.0", md5="1297d7698543b8d157dee9896aa9b468")

	depends_on("r@2.10:", type=("build", "run"))
