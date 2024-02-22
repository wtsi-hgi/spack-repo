# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGgaligner(RPackage):
	"""Visualizing Sequence Alignment by Generating Publication-Ready
Plots

	Providing publication-ready graphs for Multiple sequence alignment. Moreover, it provides a unique solution for visualizing the multiple sequence alignment without the need to do the alignment in each run which is a big limitation in other available packages.
	"""
	
	cran = "ggaligner" 

	version("0.1", md5="01779716f428a8de6ef0408ac9370779")

	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggmsa", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
