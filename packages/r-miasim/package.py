# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMiasim(RPackage):
	"""Microbiome Data Simulation

	Microbiome time series simulation with generalized Lotka-Volterra model, Self-Organized Instability (SOI), and other models. Hubbell's Neutral model is used to determine the abundance matrix. The resulting abundance matrix is applied to (Tree)SummarizedExperiment objects.
	"""
	
	homepage = "https://github.com/microbiome/miaSim"
	bioc = "miaSim" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/miaSim_1.8.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/miaSim/miaSim_1.8.0.tar.gz"]

	version("1.8.0", sha256="b3337d0e1e272271053a4f78b5e598429c76b6d0601557da466ad42bc369a3cc")

	depends_on("r-treesummarizedexperiment", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-desolve", type=("build", "run"))
	depends_on("r-powerlaw", type=("build", "run"))
	depends_on("r-matrixgenerics", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
