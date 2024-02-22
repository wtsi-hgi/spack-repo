# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAvirtualtwins(RPackage):
	"""Adaptation of Virtual Twins Method from Jared Foster

	Research of subgroups in random clinical trials with binary outcome and two treatments groups. This is an adaptation of the Jared Foster method (<https://www.ncbi.nlm.nih.gov/pubmed/21815180>).
	"""
	
	homepage = "https://github.com/prise6/aVirtualTwins"
	cran = "aVirtualTwins" 

	version("1.0.1", md5="f4e5fdb31d55a7fb8e57f09331ca393a")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-rpart", type=("build", "run"))
	depends_on("r-party", type=("build", "run"))
	depends_on("r-randomforest", type=("build", "run"))
