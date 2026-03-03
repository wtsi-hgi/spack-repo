# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPardnacopy(RPackage):
	"""Parallel implementation of the "segment" function of package
"DNAcopy"

	Parallelized version of the "segment" function from Bioconductor package "DNAcopy", utilizing multi-core computation on host CPU
	"""
	
	cran = "ParDNAcopy" 

	version("2.0", md5="c62450033305046a357e3c46db454c21")

	depends_on("r-dnacopy", type=("build", "run"))
