# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCureauxsp(RPackage):
	"""Mixture Cure Models with Auxiliary Subgroup Survival
Probabilities

	Estimate mixture cure models with subgroup survival probabilities as auxiliary information. A reference of the underlying methods is Jie Ding, Jialiang Li and Xiaoguang Wang (2024) <doi:10.1093/jrsssc/qlad106>.
	"""
	
	homepage = "<https://github.com/biostat-jieding/CureAuxSP>"
	cran = "CureAuxSP" 

	version("0.0.1", md5="dee7f47fc5de1bc00867661dd790319c")

	depends_on("r-mass", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-lars", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-tcgabiolinks", type=("build", "run"))
