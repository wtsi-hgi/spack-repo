# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RClustvarlv(RPackage):
	"""Clustering of Variables Around Latent Variables

	Functions for the clustering of variables around Latent Variables, for 2-way or 3-way data. Each cluster of variables, which may be defined as a local or directional cluster, is associated with a latent variable. External variables measured on the same observations or/and additional information on the variables can be taken into account. A "noise" cluster or sparse latent variables can also be defined.
	"""
	
	cran = "ClustVarLV" 

	version("2.1.1", md5="8b2f3f447bf48c2405e67cbb557f1760")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-iterators", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
