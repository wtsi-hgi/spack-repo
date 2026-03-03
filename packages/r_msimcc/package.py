# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMsimcc(RPackage):
	"""Micro Simulation Model for Cervical Cancer Prevention

	Micro simulation model to reproduce natural history of cervical cancer and cost-effectiveness evaluation of prevention strategies. See Georgalis L, de Sanjose S, Esnaola M, Bosch F X, Diaz M (2016) <doi:10.1097/CEJ.0000000000000202> for more details.
	"""
	
	cran = "mSimCC" 

	version("0.0.3", md5="5262922775caedab314c953c23e39eaa")

	depends_on("r@3.1.1:", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
