# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RItop(RPackage):
	"""Inferring the Topology of Omics Data

	Infers a topology of relationships between different datasets, such as multi-omics and phenotypic data recorded on the same samples. We based this methodology on the RV coefficient (Robert & Escoufier, 1976, <doi:10.2307/2347233>), a measure of matrix correlation, which we have extended for partial matrix correlations and binary data (Aben et al., 2018, <doi:10.1101/293993>).
	"""
	
	cran = "iTOP" 

	version("1.0.2", md5="8652dcae19e96e4d8b5df0efb2dbaba7")

	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-corpcor", type=("build", "run"))
