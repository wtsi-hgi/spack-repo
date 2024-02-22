# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGwasbycluster(RPackage):
	"""Identifying Significant SNPs in Genome Wide Association Studies
(GWAS) via Clustering

	Identifying disease-associated significant SNPs using clustering approach. This package is implementation of method proposed in Xu et al (2019) <DOI:10.1038/s41598-019-50229-6>.
	"""
	
	cran = "GWASbyCluster" 

	version("0.1.7", md5="8095e2fb42db53b2d7980e02d4072ade")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-snpstats", type=("build", "run"))
	depends_on("r-rootsolve", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
