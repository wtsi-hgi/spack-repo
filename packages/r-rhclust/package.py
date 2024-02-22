# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRhclust(RPackage):
	"""Vector in Partition

	Non-parametric clustering of joint pattern multi-genetic/epigenetic factors. This package contains functions designed to cluster subjects based on gene features including single nucleotide polymorphisms (SNPs), DNA methylation (CPG), gene expression (GE), and covariate data. The novel concept follows the general K-means (Hartigan and Wong (1979) <doi:10.2307/2346830> framework but uses weighted Euclidean distances across the gene features to cluster subjects. This approach is unique in that it attempts to capture all pairwise interactions in an effort to cluster based on their complex biological interactions.
	"""
	
	cran = "RHclust" 

	version("2.0.0", md5="8853e543ccdae7537b933bcc1fae0e06")

	depends_on("r-runuran", type=("build", "run"))
