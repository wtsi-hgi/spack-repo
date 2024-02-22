# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRcnv(RPackage):
	"""Detect Copy Number Variants from SNPs Data

	Functions in this package will import filtered variant call format (VCF) files of SNPs data and generate data sets to detect copy number variants, visualize them and do downstream analyses with copy number variants(e.g. Environmental association analyses).
	"""
	
	homepage = "https://piyalkarum.github.io/rCNV/"
	cran = "rCNV" 

	version("1.2.0", md5="54877650f4063b83bafd52a1ee0f88cd")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-colorspace", type=("build", "run"))
	depends_on("r-r-utils", type=("build", "run"))
	depends_on("r-qgraph", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
