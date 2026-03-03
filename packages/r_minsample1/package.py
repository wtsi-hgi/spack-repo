# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMinsample1(RPackage):
	"""The Minimum Sample Size

	Using this package, one can determine the minimum sample size required so that the absolute deviation of the sample mean and the population mean of a distribution becomes less than some pre-determined epsilon, i.e. it helps the user to determine the minimum sample size required to attain the pre-fixed precision level by minimizing the difference between the sample mean and population mean. 
	"""
	
	cran = "minsample1" 

	version("0.1.0", md5="e0b462dcc22ed7fd92d6ef071173fffe", url="https://cran.r-project.org/src/contrib/minsample1_0.1.0.tar.gz")

