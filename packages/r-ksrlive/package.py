# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKsrlive(RPackage):
	"""Identify Kinase Substrate Relationships Using Dynamic Data

	Using this package you can combine known kinase substrate relationships with experimental data and determine active kinases and their substrates.
	"""
	
	cran = "ksrlive" 

	version("1.0", md5="ea656ec60959729a3000cfbeeea3b572")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-tightclust", type=("build", "run"))
