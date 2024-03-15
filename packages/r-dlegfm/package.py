# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDlegfm(RPackage):
	"""Distributed Loading Estimation for General Factor Model

	The load estimation method is based on a general factor model to solve the estimates of load and specific variance. The philosophy of the package is described in Guangbao Guo. (2022). <doi:10.1007/s00180-022-01270-z>.
	"""
	
	cran = "DLEGFM" 

	version("0.4.0", md5="57f58591bfffc59deb0557bec66ba983")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-elasticnet", type=("build", "run"))
