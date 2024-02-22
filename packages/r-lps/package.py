# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLps(RPackage):
	"""Linear Predictor Score, for Binary Inference from Multiple
Continuous Variables

	An implementation of the Linear Predictor Score approach, as initiated by Radmacher et al. (J Comput Biol 2001) and enhanced by Wright et al. (PNAS 2003) for gene expression signatures. Several tools for unsupervised clustering of gene expression data are also provided.
	"""
	
	homepage = "https://bioinformatics.ovsa.fr/LPS"
	cran = "LPS" 

	version("1.0.16", md5="e81ea7f42d500538ba7370ec62e2736d")

	depends_on("r@2.10:", type=("build", "run"))
