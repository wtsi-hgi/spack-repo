# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RClusterrepro(RPackage):
	"""Reproducibility of Gene Expression Clusters

	This is a function for validating microarray clusters via reproducibility,
 based on the paper referenced below.
	"""
	
	homepage = "https://www.ncbi.nlm.nih.gov/pubmed/16613834."
	cran = "clusterRepro" 

	version("0.9", md5="23577a5fc8b7520382a9cfe001185df5")

	depends_on("r@2.2:", type=("build", "run"))
