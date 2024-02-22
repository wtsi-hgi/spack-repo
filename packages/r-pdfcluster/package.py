# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPdfcluster(RPackage):
	"""Cluster Analysis via Nonparametric Density Estimation

	Cluster analysis via nonparametric density 
   estimation is performed. Operationally, the kernel method is used throughout to estimate
   the density. Diagnostics methods for evaluating the quality of the clustering 
   are available. The package includes also a routine to estimate the 
   probability density function obtained by the kernel method, given a set of
   data with arbitrary dimensions.
	"""
	
	cran = "pdfCluster" 

	version("1.0-4", md5="44977c813b151392cc3c91c8403e048e")

	depends_on("r-geometry", type=("build", "run"))
