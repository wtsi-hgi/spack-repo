# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQrisk3(RPackage):
	"""10-Year Cardiovascular Disease Risk Calculator (QRISK3 2017)

	This function aims to calculate risk of developing cardiovascular disease of individual patients in next 10 years. This unofficial package was based on published open-sourced free risk prediction algorithm QRISK3-2017 <https://qrisk.org/src.php>. 
	"""
	
	cran = "QRISK3" 

	version("0.6.0", md5="5b4eb181d0d096669c279b5a82a8df93", url="https://cran.r-project.org/src/contrib/QRISK3_0.6.0.tar.gz")

