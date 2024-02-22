# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMinsample2(RPackage):
	"""The Minimum Sample Size

	Using this package, one can determine the minimum sample size required so that the mean square error of the sample mean and the population mean of a distribution becomes less than some pre-determined epsilon, i.e. it helps the user to determine the minimum sample size required to attain the pre-fixed precision level by minimizing the difference between the sample mean and population mean. 
	"""
	
	cran = "minsample2" 

	version("0.1.0", md5="1536f145f1328e27031950ad16f9882d", url="https://cran.r-project.org/src/contrib/minsample2_0.1.0.tar.gz")

