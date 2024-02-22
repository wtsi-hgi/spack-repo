# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAmpliconduo(RPackage):
	"""Statistical Analysis of Amplicon Data of the Same Sample to
Identify Artefacts

	Increasingly powerful techniques for high-throughput sequencing open the possibility to comprehensively characterize microbial communities, including rare species. However, a still unresolved issue are the substantial error rates in the experimental process generating these sequences. To overcome these limitations we propose an approach, where each sample is split and the same amplification and sequencing protocol is applied to both halves. This procedure should allow to detect likely PCR and sequencing artifacts, and true rare species by comparison of the results of both parts. The AmpliconDuo package, whereas amplicon duo from here on refers to the two amplicon data sets of a split sample, is intended to help interpret the obtained read frequency distribution across split samples, and to filter the false positive reads.
	"""
	
	cran = "AmpliconDuo" 

	version("1.1.1", md5="9d8bc69ee29b3cb612b6e819198c258a")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-xtable", type=("build", "run"))
