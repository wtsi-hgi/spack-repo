# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLcda(RPackage):
	"""Latent Class Discriminant Analysis

	Providing a method for Local Discrimination via Latent Class Models. The approach is described in <https://www.r-project.org/conferences/useR-2009/abstracts/pdf/Bucker.pdf>.
	"""
	
	cran = "lcda" 

	version("0.3.2", md5="77ca889d80a941bcd4a8e41a5cf8121a")

	depends_on("r@2.6:", type=("build", "run"))
	depends_on("r-polca", type=("build", "run"))
