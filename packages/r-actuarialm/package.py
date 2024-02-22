# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RActuarialm(RPackage):
	"""Computation of Actuarial Measures Using Bell G Family

	It computes two frequently applied actuarial measures, the expected shortfall and the value at risk. Seven well-known classical distributions in connection to the Bell generalized family are used as follows: Bell-exponential distribution, Bell-extended exponential distribution, Bell-Weibull distribution, Bell-extended Weibull distribution, Bell-Lomax distribution, Bell-Burr-12 distribution, and Bell-Burr-X distribution. Related works include:
     a) Fayomi, A., Tahir, M. H., Algarni, A., Imran, M., & Jamal, F. (2022). "A new useful exponential model with applications to quality control and 
        actuarial data". Computational Intelligence and Neuroscience, 2022. <doi:10.1155/2022/2489998>.
     b) Alsadat, N., Imran, M., Tahir, M. H., Jamal, F., Ahmad, H., & Elgarhy, M. (2023). "Compounded Bell-G class of statistical models with applications to COVID-19 and actuarial data". Open Physics, 21(1), 20220242. <doi:10.1515/phys-2022-0242>.
	"""
	
	cran = "ActuarialM" 

	version("0.1.0", md5="68749e879b6d498dad258b08cd31ffa6")

	depends_on("r@2:", type=("build", "run"))
