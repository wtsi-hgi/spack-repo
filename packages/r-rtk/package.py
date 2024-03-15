# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRtk(RPackage):
	"""Rarefaction Tool Kit

	Rarefy data, calculate diversity and plot the results.
	"""
	
	cran = "rtk" 

	version("0.2.6.1", md5="4a7b2bb683c7cc1e7ae16baf39cd0ebe")

	depends_on("r-rcpp", type=("build", "run"))
