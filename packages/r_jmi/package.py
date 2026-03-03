# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RJmi(RPackage):
	"""Jackknife Mutual Information

	Computes the Jackknife Mutual Information (JMI) between two random vectors and provides the p-value for dependence tests. See Zeng, X., Xia, Y. and Tong, H. (2018) <doi:10.1073/pnas.1715593115>.
	"""
	
	cran = "JMI" 

	version("0.1.0", md5="42ea8feba0766d7ba90d12168ed90480")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
