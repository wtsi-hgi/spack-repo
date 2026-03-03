# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSimcormultres(RPackage):
	"""Simulates Correlated Multinomial Responses

	Simulates correlated multinomial responses conditional on a marginal model specification.
	"""
	
	homepage = "https://github.com/AnestisTouloumis/SimCorMultRes"
	cran = "SimCorMultRes" 

	version("1.9.0", md5="de41fefde5f7dcb995e8969df2806dfd")

	depends_on("r@2.15:", type=("build", "run"))
	depends_on("r-evd", type=("build", "run"))
