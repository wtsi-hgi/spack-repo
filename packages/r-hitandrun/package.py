# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHitandrun(RPackage):
	""""Hit and Run" and "Shake and Bake" for Sampling Uniformly from
Convex Shapes

	The "Hit and Run" Markov Chain Monte Carlo method for sampling uniformly from convex shapes defined by linear constraints, and the "Shake and Bake" method for sampling from the boundary of such shapes. Includes specialized functions for sampling normalized weights with arbitrary linear constraints. Tervonen, T., van Valkenhoef, G., Basturk, N., and Postmus, D. (2012) <doi:10.1016/j.ejor.2012.08.026>. van Valkenhoef, G., Tervonen, T., and Postmus, D. (2014) <doi:10.1016/j.ejor.2014.06.036>.
	"""
	
	homepage = "https://github.com/gertvv/hitandrun"
	cran = "hitandrun" 

	version("0.5-6", md5="9cd8d97bf15fbcfb09f4307cf308a107")

	depends_on("r-rcdd@1.1:", type=("build", "run"))
