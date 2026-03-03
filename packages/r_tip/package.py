# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTip(RPackage):
	"""Bayesian Clustering Using the Table Invitation Prior (TIP)

	Cluster data without specifying the number of clusters using the Table Invitation Prior (TIP) introduced in the paper "Clustering Gene Expression Using the Table Invitation Prior" by Charles W. Harrison, Qing He, and Hsin-Hsiung Huang (2022) <doi:10.3390/genes13112036>. TIP is a Bayesian prior that uses pairwise distance and similarity information to cluster vectors, matrices, or tensors.
	"""
	
	cran = "tip" 

	version("0.1.0", md5="5d9a2b64689d021879bf144f0b1acf4a")

	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-network", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggally", type=("build", "run"))
	depends_on("r-laplacesdemon", type=("build", "run"))
	depends_on("r-changepoint", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-mniw", type=("build", "run"))
