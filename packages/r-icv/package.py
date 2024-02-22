# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIcv(RPackage):
	"""Indirect Cross-Validation (ICV) for Kernel Density Estimation

	Functions for computing the global and local Gaussian density estimates based on the ICV bandwidth. See the article of Savchuk, O.Y., Hart, J.D., Sheather, S.J. (2010). Indirect cross-validation for density estimation. Journal of the American Statistical Association, 105(489), 415-423 <doi:10.1198/jasa.2010.tm08532>.
	"""
	
	cran = "ICV" 

	version("1.0", md5="53d551bcfbbbf9903f358a8462ea8889")

	depends_on("r@3.1.1:", type=("build", "run"))
