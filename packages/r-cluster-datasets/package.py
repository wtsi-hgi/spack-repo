# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RClusterDatasets(RPackage):
	"""Cluster Analysis Data Sets

	A collection of data sets for teaching cluster analysis.
	"""
	
	cran = "cluster.datasets" 

	version("1.0-1", md5="04adbeaecbf6c2348c6433b6bbe3b3a9")

	depends_on("r@2.0.1:", type=("build", "run"))
