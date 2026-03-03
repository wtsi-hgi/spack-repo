# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RElections(RPackage):
	"""USA Presidential Elections Data

	This includes a dataset on the outcomes of the USA presidential elections since 1920, and various predictors, as used in <https://www.vanderwalresearch.com/blog/15-elections>.
	"""
	
	cran = "elections" 

	version("1.0.1", md5="ded705b46c333aca596216cf95e2755c")

	depends_on("r@3:", type=("build", "run"))
