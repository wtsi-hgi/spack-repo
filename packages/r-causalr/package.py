# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCausalr(RPackage):
	"""Causal network analysis methods

	Causal network analysis methods for regulator prediction and network reconstruction from genome scale data.
	"""
	
	bioc = "CausalR" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/CausalR_1.34.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/CausalR/CausalR_1.34.0.tar.gz"]

	version("1.34.0", md5="408b3cc6bc7a45715e6c07095f61ca2b")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
