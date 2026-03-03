# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRepmod(RPackage):
	"""Create Report Table from Different Objects

	Tools for generating descriptives and report tables for different models,
    data.frames and tables and exporting them to different formats.
	"""
	
	cran = "repmod" 

	version("0.1.7", md5="713f87ea2896d9f0d43f3851b60d60a2")

	depends_on("r-boot", type=("build", "run"))
	depends_on("r-flextable", type=("build", "run"))
	depends_on("r-lme4", type=("build", "run"))
	depends_on("r-lmertest", type=("build", "run"))
	depends_on("r-officer", type=("build", "run"))
	depends_on("r-xtable", type=("build", "run"))
