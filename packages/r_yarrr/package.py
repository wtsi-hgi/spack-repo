# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RYarrr(RPackage):
	"""A Companion to the e-Book "YaRrr!: The Pirate's Guide to R"

	Contains a mixture of functions and data sets referred to in the introductory e-book "YaRrr!: The Pirate's Guide to R". The latest version of the e-book is available for free at <https://www.thepiratesguidetor.com>.
	"""
	
	homepage = "www.thepiratesguidetor.com"
	cran = "yarrr" 

	version("0.1.5", md5="bd33188e7ffb2931e948a7c445b30cbd")

	depends_on("r-jpeg", type=("build", "run"))
	depends_on("r-bayesfactor", type=("build", "run"))
	depends_on("r-circlize", type=("build", "run"))
