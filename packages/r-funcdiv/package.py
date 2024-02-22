# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFuncdiv(RPackage):
	"""Compute Contributional Diversity Metrics

	Compute alpha and beta contributional diversity metrics,
    which is intended for linking taxonomic and functional microbiome
    data. See 'GitHub' repository for the tutorial:
    <https://github.com/gavinmdouglas/FuncDiv/wiki>. Citation: Gavin M.
    Douglas, Sunu Kim, Morgan G. I. Langille, B. Jesse Shapiro (2023)
    <doi:10.1093/bioinformatics/btac809>.
	"""
	
	cran = "FuncDiv" 

	version("1.0.0", md5="b371b58457ac9cd7c2ff85c7c5263401")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ape", type=("build", "run"))
	depends_on("r-collapse", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-paralleldist", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcppparallel", type=("build", "run"))
	depends_on("r-rcppxptrutils", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
