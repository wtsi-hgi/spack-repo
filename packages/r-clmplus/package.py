# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RClmplus(RPackage):
	"""Tool-Box of Chain Ladder Plus Models

	Implementation of the chain ladder model under the reverse time framework
    introduced in Hiabu (2017) <doi:10.1080/03461238.2016.1240709>.
    It also implements extensions that add flexibility to the individual development factors modeling
    by allowing practitioners to set their own hazard rate model.
	"""
	
	homepage = "https://github.com/gpitt71/clmplus"
	cran = "clmplus" 

	version("0.1.0", md5="3c60d1efa3ff2647465b49c2406054c8")

	depends_on("r-stmomo", type=("build", "run"))
	depends_on("r-chainladder", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-forecast", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
