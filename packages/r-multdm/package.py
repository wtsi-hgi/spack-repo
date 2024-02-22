# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMultdm(RPackage):
	"""Multivariate Version of the Diebold-Mariano Test

	Allows to perform the multivariate version of the Diebold-Mariano test for equal predictive ability of multiple forecast comparison. Main reference: Mariano, R.S., Preve, D. (2012) <doi:10.1016/j.jeconom.2012.01.014>. 
	"""
	
	homepage = "https://CRAN.R-project.org/package=multDM"
	cran = "multDM" 

	version("1.1.4", md5="713ebc5647b78d0950b8bb4b74aaf1e7")

	depends_on("r-mts", type=("build", "run"))
