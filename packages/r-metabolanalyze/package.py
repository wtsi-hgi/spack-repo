# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMetabolanalyze(RPackage):
	"""Probabilistic Latent Variable Models for Metabolomic Data

	Fits probabilistic principal components analysis,
        probabilistic principal components and covariates analysis and
        mixtures of probabilistic principal components models to
        metabolomic spectral data.
	"""
	
	cran = "MetabolAnalyze" 

	version("1.3.1", md5="486d109cb4c42bd07f747549fce95344")

	depends_on("r-mclust", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-ellipse", type=("build", "run"))
	depends_on("r-gtools", type=("build", "run"))
	depends_on("r-gplots", type=("build", "run"))
