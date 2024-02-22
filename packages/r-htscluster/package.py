# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHtscluster(RPackage):
	"""Clustering High-Throughput Transcriptome Sequencing (HTS) Data

	A Poisson mixture model is implemented to cluster genes from high-
    throughput transcriptome sequencing (RNA-seq) data. Parameter estimation is
    performed using either the EM or CEM algorithm, and the slope heuristics are
    used for model selection (i.e., to choose the number of clusters).
	"""
	
	cran = "HTSCluster" 

	version("2.0.11", md5="4177fa3e8f47759d706fb4cc046729df")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-edger", type=("build", "run"))
	depends_on("r-plotrix", type=("build", "run"))
	depends_on("r-capushe", type=("build", "run"))
