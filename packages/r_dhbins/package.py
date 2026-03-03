# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDhbins(RPackage):
	"""Hexmaps for NZ District Health Boards

	Draws stylized choropleth maps -- hexagonal maps and triangular multiclass hex maps -- for New Zealand District Health Boards and Regional Council areas. These allow faceted, coloured displays of quantitative information for comparison across District Health Boards or Regional Councils. The preprint Lumley (2019) <arXiv:1912.04435> is based on the methods in this package.
	"""
	
	cran = "DHBins" 

	version("1.1", md5="6d082e7c4b35c9e5e926e760b316d5ab")

	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r@3.6:", type=("build", "run"))
