# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFcuk(RPackage):
	"""The Ultimate Helper for Clumsy Fingers

	Automatically suggests a correction when a typo occurs.
	"""
	
	homepage = "https://github.com/ThinkRstat/fcuk"
	cran = "fcuk" 

	version("0.1.21", md5="2d4ade71dbefd2dd05e76a6e09f124e3")

	depends_on("r-stringdist", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
