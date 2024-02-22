# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RJackknifer(RPackage):
	"""Delete-d Jackknife for Point and Interval Estimation

	This function creates jackknife samples from the data by
    sequentially removing d observations from the data, performs
    estimation using the jackknife samples and calculates the jackknife
    coefficients, bias, standard error and confidence intervals based on
    the methodology discussed by Quenouille (1956) <doi:10.2307/2332914>,
    Tukey (1958) <doi:10.1214/aoms/1177706647> and Shi (1988)
    <doi:10.1016/0167-7152(88)90011-9>.
	"""
	
	cran = "jackknifeR" 

	version("1.2.0", md5="837aa986b1184552fa3bf3c1ce7f1481")

	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
