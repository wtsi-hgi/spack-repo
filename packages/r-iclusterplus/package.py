# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIclusterplus(RPackage):
	"""Integrative clustering of multi-type genomic data

	Integrative clustering of multiple genomic data using a joint latent variable model.
	"""
	
	bioc = "iClusterPlus" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/iClusterPlus_1.38.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/iClusterPlus/iClusterPlus_1.38.0.tar.gz"]

	version("1.38.0", md5="133b682823ec6ab41f6f6579413d461d")

	depends_on("r@4.1:", type=("build", "run"))
