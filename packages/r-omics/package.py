# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROmics(RPackage):
	"""'--omics' Data Analysis Toolbox

	A collection of functions to analyse '--omics' datasets such as DNA
    methylation and gene expression profiles.
	"""
	
	cran = "omics" 

	version("0.1-5", md5="a9f62a95ed46f95056766e4ab2b1f038")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-lme4", type=("build", "run"))
	depends_on("r-pheatmap", type=("build", "run"))
