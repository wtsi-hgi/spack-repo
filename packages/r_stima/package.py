# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStima(RPackage):
	"""Simultaneous Threshold Interaction Modeling Algorithm

	Regression trunk model estimation proposed by Dusseldorp and Meulman (2004) <doi:10.1007/bf02295641> and Dusseldorp, Conversano, Van Os (2010) <doi:10.1198/jcgs.2010.06089>, integrating a regression tree and a multiple regression model.   
	"""
	
	cran = "stima" 

	version("1.2.4", md5="52d608dc40ccd4eaaf9cfc70bdadd56a")

	depends_on("r@3.0.2:", type=("build", "run"))
	depends_on("r-rpart", type=("build", "run"))
