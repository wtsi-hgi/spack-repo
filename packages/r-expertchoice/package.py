# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RExpertchoice(RPackage):
	"""Design of Discrete Choice and Conjoint Analysis

	Supports designing efficient discrete choice experiments (DCEs). Experimental designs can be formed on the basis of orthogonal arrays or search methods for optimal designs (Federov or mixed integer programs). Various methods for converting these experimental designs into a discrete choice experiment. Many efficiency measures! Draws from literature of Kuhfeld (2010) and Street et. al (2005) <doi:10.1016/j.ijresmar.2005.09.003>.
	"""
	
	cran = "ExpertChoice" 

	version("0.2.0", md5="44a660aa2337541a3b7094a757b89842")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-far", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-doe-base", type=("build", "run"))
	depends_on("r-rlist", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
