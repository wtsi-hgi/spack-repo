# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMurphydiagram(RPackage):
	"""Murphy Diagrams for Forecast Comparisons

	Data and code for the paper by Ehm, Gneiting, Jordan and
    Krueger ('Of Quantiles and Expectiles: Consistent Scoring Functions, Choquet
    Representations, and Forecast Rankings', JRSS-B, 2016 <DOI:10.1111/rssb.12154>).
	"""
	
	homepage = "https://sites.google.com/site/fk83research/code"
	cran = "murphydiagram" 

	version("0.12.2", md5="fcc8cb152293e3d701bd9eefe3ba7e32")

