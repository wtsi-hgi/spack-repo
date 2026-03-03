# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTreefit(RPackage):
	"""The First Software for Quantitative Trajectory Inference

	Perform two types of analysis: 1) checking the
    goodness-of-fit of tree models to your single-cell gene expression
    data; and 2) deciding which tree best fits your data.
	"""
	
	homepage = "https://hayamizu-lab.github.io/treefit-r/"
	cran = "treefit" 

	version("1.0.2", md5="661f443884221dd63885e1ee0d6466f9")

	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-patchwork", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
