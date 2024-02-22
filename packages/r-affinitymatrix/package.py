# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAffinitymatrix(RPackage):
	"""Estimation of Affinity Matrix

	Tools to study sorting patterns in matching markets and to estimate the affinity matrix of both the bipartite one-to-one matching model without frictions and with Transferable Utility by 'Dupuy' and 'Galichon' (2014) <doi:10.1086/677191> and its 'unipartite' variant by 'Ciscato', 'Galichon' and 'Gousse' (2020) <doi:10.1086/704611>. It also contains all the necessary tools to implement the 'saliency' analysis, to run rank tests of the affinity matrix and to build tables and plots summarizing the findings.
	"""
	
	cran = "affinitymatrix" 

	version("0.1.0", md5="4b8a74aedddcf0d3b7b94035e3589efa")

	depends_on("r-expm", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-hmisc", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
