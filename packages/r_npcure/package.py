# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNpcure(RPackage):
	"""Nonparametric Estimation in Mixture Cure Models

	Performs nonparametric estimation in mixture cure models, and significance tests for the cure probability. For details, see López-Cheda et al. (2017a) <doi:10.1016/j.csda.2016.08.002> and López-Cheda et al. (2017b) <doi:10.1007/s11749-016-0515-1>.
	"""
	
	cran = "npcure" 

	version("0.1-5", md5="4b8f26366f322bceb4004b8df65d05fc")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-permute", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
