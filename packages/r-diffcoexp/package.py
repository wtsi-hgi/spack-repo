# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDiffcoexp(RPackage):
	"""Differential Co-expression Analysis

	A tool for the identification of differentially coexpressed links (DCLs) and differentially coexpressed genes (DCGs). DCLs are gene pairs with significantly different correlation coefficients under two conditions. DCGs are genes with significantly more DCLs than by chance.
	"""
	
	homepage = "https://github.com/hidelab/diffcoexp"
	bioc = "diffcoexp"

	version("1.28.0", commit="32abc42a2dddadc2c1d8e4daffe692c66be3b98f")
	version("1.22.0", commit="d903fab0c59c7b9818b7c42f75cb21a874b54aa3")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-wgcna", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-diffcorr", type=("build", "run"))
	depends_on("r-psych", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
