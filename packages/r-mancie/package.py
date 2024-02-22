# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMancie(RPackage):
	"""Matrix Analysis and Normalization by Concordant Information
Enhancement

	High-dimensional data integration is a critical but difficult problem in genomics research because of potential biases from high-throughput experiments. We present MANCIE, a computational method for integrating two genomic data sets with homogenous dimensions from different sources based on a PCA procedure as an approximation to a Bayesian approach.
	"""
	
	cran = "MANCIE" 

	version("1.4", md5="bc6a5f80e1f7f420aebe0df37e1aa2af")

	depends_on("r@2.15:", type=("build", "run"))
