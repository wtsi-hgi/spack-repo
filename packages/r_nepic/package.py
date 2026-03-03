# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNepic(RPackage):
	"""Network Assisted Algorithm for Epigenetic Studies Using Mean and
Variance Combined Signals

	Package for a Network assisted algorithm for Epigenetic studies using mean and variance Combined signals: NEpiC. NEpiC combines both signals in mean and variance differences in methylation level between case and control groups searching for differentially methylated sub-networks (modules) using the protein-protein interaction network.
	"""
	
	cran = "NEpiC" 

	version("1.0.1", md5="d4badc091bcf7f65950ba203f104d18f")

	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-paireddata", type=("build", "run"))
