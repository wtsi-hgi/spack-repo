# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRsstest(RPackage):
	"""Testing the Equality of Two Means Using RSS and MRSS

	Testing the equality of two means using Ranked Set Sampling
             and Median Ranked Set Sampling are provided under normal distribution. Data generation functions are also given RSS and MRSS. 
             Also, data generation functions are given under imperfect ranking data for Ranked Set Sampling and Median Ranked Set Sampling.
             Ozdemir Y.A., Ebegil M., & Gokpinar F. (2019), <doi:10.1007/s40995-018-0558-0>
             Ozdemir Y.A., Ebegil M., & Gokpinar F. (2017), <doi:10.1080/03610918.2016.1263736>.
	"""
	
	cran = "RSStest" 

	version("1.0", md5="5e7cea69825b28e89629499fbe2286c2")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-huxtable@5.4:", type=("build", "run"))
