# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPcalg(RPackage):
	"""Methods for Graphical Models and Causal Inference

	Functions for causal structure
  learning and causal inference using graphical models. The main algorithms
  for causal structure learning are PC (for observational data without hidden
  variables), FCI and RFCI (for observational data with hidden variables),
  and GIES (for a mix of data from observational studies
  (i.e. observational data) and data from experiments
  involving interventions (i.e. interventional data) without hidden
  variables). For causal inference the IDA algorithm, the Generalized
  Backdoor Criterion (GBC), the Generalized Adjustment Criterion (GAC)
  and some related functions are implemented. Functions for incorporating
  background knowledge are provided.
	"""
	
	homepage = "https://pcalg.r-forge.r-project.org/"
	cran = "pcalg" 

	version("2.7-11", md5="4f6e7f843d71ecf79d78a9c9c85ed54d")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-abind", type=("build", "run"))
	depends_on("r-graph", type=("build", "run"))
	depends_on("r-rbgl", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-ggm", type=("build", "run"))
	depends_on("r-corpcor", type=("build", "run"))
	depends_on("r-robustbase", type=("build", "run"))
	depends_on("r-vcd", type=("build", "run"))
	depends_on("r-rcpp@0.11:", type=("build", "run"))
	depends_on("r-bdsmatrix", type=("build", "run"))
	depends_on("r-sfsmisc@1.0.26:", type=("build", "run"))
	depends_on("r-fastica", type=("build", "run"))
	depends_on("r-clue", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
	depends_on("r-bh", type=("build", "run"))
