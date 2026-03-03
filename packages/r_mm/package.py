# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMm(RPackage):
	"""The Multiplicative Multinomial Distribution

	Various utilities for the Multiplicative Multinomial distribution.
	"""
	
	homepage = "https://github.com/RobinHankin/MM"
	cran = "MM" 

	version("1.6-7", md5="64078c4de260e78ecf99894fefc5176f")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-oarray@1.4.6:", type=("build", "run"))
	depends_on("r-partitions@1.9.14:", type=("build", "run"))
	depends_on("r-magic@1.5.6:", type=("build", "run"))
	depends_on("r-abind", type=("build", "run"))
	depends_on("r-emulator@1.2.13:", type=("build", "run"))
	depends_on("r-mathjaxr", type=("build", "run"))
