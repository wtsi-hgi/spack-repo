# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RUntb(RPackage):
	"""Ecological Drift under the UNTB

	Hubbell's Unified Neutral Theory of Biodiversity.
	"""
	
	homepage = "https://github.com/RobinHankin/untb"
	cran = "untb" 

	version("1.7-7", md5="1d5176fc2090669ce866445cd44aef81")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-brobdingnag@1.1.8:", type=("build", "run"))
	depends_on("r-partitions@1.9.14:", type=("build", "run"))
	depends_on("r-polynom", type=("build", "run"))
