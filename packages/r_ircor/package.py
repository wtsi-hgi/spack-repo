# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIrcor(RPackage):
	"""Correlation Coefficients for Information Retrieval

	Provides implementation of various correlation coefficients of common use in
  Information Retrieval. In particular, it includes Kendall (1970, isbn:0852641990) tau coefficient
  as well as tau_a and tau_b for the treatment of ties. It also includes Yilmaz et al. (2008)
  <doi:10.1145/1390334.1390435> tauAP correlation coefficient, and versions tauAP_a and tauAP_b
  developed by Urbano and Marrero (2017) <doi:10.1145/3121050.3121106> to cope with ties.
	"""
	
	homepage = "https://github.com/julian-urbano/ircor/"
	cran = "ircor" 

	version("1.0", md5="b3f1ac3f3b211905b6b836a3fc009778")

	depends_on("r@3.2:", type=("build", "run"))
