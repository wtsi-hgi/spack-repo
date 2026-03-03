# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSurvsim(RPackage):
	"""Simulation of Simple and Complex Survival Data

	Simulation of simple and complex survival data including recurrent and multiple events and competing risks. See Moriña D, Navarro A. (2014) <doi:10.18637/jss.v059.i02> and Moriña D, Navarro A. (2017) <doi:10.1080/03610918.2016.1175621>.
	"""
	
	cran = "survsim" 

	version("1.1.8", md5="25638c3e9d5daf7d07726569498fb4df")

	depends_on("r@2.13.1:", type=("build", "run"))
	depends_on("r-eha", type=("build", "run"))
	depends_on("r-statmod", type=("build", "run"))
