# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROpc(RPackage):
	"""The Online Principal Component Estimation Method

	The online principal component method can process the online data set. The philosophy of the package is described in Guo G. (2018) <doi:10.1080/10485252.2018.1531130>.
	"""
	
	cran = "OPC" 

	version("0.0.2", md5="9e9fddb06315a80096f3b19696d462d8")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
