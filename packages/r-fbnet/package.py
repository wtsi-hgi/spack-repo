# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFbnet(RPackage):
	"""Forensic Bayesian Networks

	Open-source package for computing likelihood ratios in kinship testing and human identification cases (Chernomoretz et al. (2021) <doi:10.1016/j.fsir.2020.100132>). It has the core function of the software GENis, developed by Fundación Sadosky. It relies on a Bayesian Networks framework and is particularly well suited to efficiently perform large-size queries against databases of missing individuals (Darwiche (2009) <doi:10.1017/CBO9780511811357>).
	"""
	
	homepage = "https://github.com/MarsicoFL/fbnet"
	cran = "fbnet" 

	version("1.0.3", md5="5c004785e94831c3b8aee4706eb3491e")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-rsolnp", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-paramlink", type=("build", "run"))
