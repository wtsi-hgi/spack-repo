# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRsca(RPackage):
	"""An R Package for Stepwise Cluster Analysis

	A statistical tool for multivariate modeling and clustering using stepwise cluster analysis. The modeling output of rSCA is constructed as a cluster tree to represent the complicated relationships between multiple dependent and independent variables. A free tool (named rSCA Tree Generator) for visualizing the cluster tree from rSCA is also released and it can be downloaded at <https://rscatree.weebly.com/>.
	"""
	
	cran = "rSCA" 

	version("3.1", md5="cbcbfe525824a8be132a209471f0d9f1")

	depends_on("r@2.10:", type=("build", "run"))
