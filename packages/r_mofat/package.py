# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMofat(RPackage):
	"""Maximum One-Factor-at-a-Time Designs

	Identifying important factors from a large number of potentially important factors of a highly nonlinear and computationally expensive black box model is a difficult problem. Xiao, Joseph, and Ray (2022) <doi:10.1080/00401706.2022.2141897> proposed Maximum One-Factor-at-a-Time (MOFAT) designs for doing this. A MOFAT design can be viewed as an improvement to the random one-factor-at-a-time (OFAT) design proposed by Morris (1991) <doi:10.1080/00401706.1991.10484804>. The improvement is achieved by exploiting the connection between Morris screening designs and Monte Carlo-based Sobol' designs, and optimizing the design using a space-filling criterion. This work is supported by a U.S. National Science Foundation (NSF) grant CMMI-1921646 <https://www.nsf.gov/awardsearch/showAward?AWD_ID=1921646>.
	"""
	
	cran = "MOFAT" 

	version("1.0", md5="c4a7c7be52fc15a292970a25d7f85c10")

	depends_on("r-slhd", type=("build", "run"))
