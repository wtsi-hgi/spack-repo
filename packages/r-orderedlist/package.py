# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROrderedlist(RPackage):
	"""Similarities of Ordered Gene Lists

	Detection of similarities between ordered lists of genes. Thereby, either simple lists can be compared or gene expression data can be used to deduce the lists. Significance of similarities is evaluated by shuffling lists or by resampling in microarray data, respectively.
	"""
	
	homepage = "http://compdiag.molgen.mpg.de/software/OrderedList.shtml"
	bioc = "OrderedList"

	version("1.80.0", commit="1b3538f17a07e07c0770c76b987ed17302d00437")
	version("1.74.0", commit="4ec2d2359a8f2e9c4f3f628a4bb27f072f3db02d")

	depends_on("r@3.6.1:", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-twilight", type=("build", "run"))
