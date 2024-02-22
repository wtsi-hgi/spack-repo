# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAmim(RPackage):
	"""Compute the Adjusted Market Inefficiency Measure

	Fast tool to calculate the Adjusted Market Inefficiency Measure following Tran & Leirvik (2019) <doi:10.1016/j.frl.2019.03.004>. This tool provides rolling window estimates of the Adjusted Market Inefficiency Measure for multiple instruments simultaneously. 
	"""
	
	homepage = "https://github.com/gelotran/AMIM"
	cran = "AMIM" 

	version("1.0.0", md5="fdb72cb8aa1932602e96e4735d6f49f4")

	depends_on("r@3.10:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
