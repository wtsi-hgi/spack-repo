# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTwl(RPackage):
	"""Two-Way Latent Structure Clustering Model

	Implementation of a Bayesian two-way latent structure model for integrative genomic clustering.  The model clusters samples in relation to distinct data sources, with each subject-dataset receiving a latent cluster label, though cluster labels have across-dataset meaning because of the model formulation.  A common scaling across data sources is unneeded, and inference is obtained by a Gibbs Sampler.  The model can fit multivariate Gaussian distributed clusters or a heavier-tailed modification of a Gaussian density.  Uniquely among integrative clustering models, the formulation makes no nestedness assumptions of samples across data sources -- the user can still fit the model if a study subject only has information from one data source. The package provides a variety of post-processing functions for model examination including ones for quantifying observed alignment of clusterings across genomic data sources.  Run time is optimized so that analyses of datasets on the order of thousands of features on fewer than 5 datasets and hundreds of subjects can converge in 1 or 2 days on a single CPU.  See "Swanson DM, Lien T, Bergholtz H, Sorlie T, Frigessi A, Investigating Coordinated Architectures Across Clusters in Integrative Studies: a Bayesian Two-Way Latent Structure Model, 2018, <doi:10.1101/387076>, Cold Spring Harbor Laboratory" at <https://www.biorxiv.org/content/early/2018/08/07/387076.full.pdf> for model details.
	"""
	
	cran = "twl" 

	version("1.0", md5="3cc72ff10eb8886f1765677a11940f15")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-mcmcpack", type=("build", "run"))
	depends_on("r-corrplot", type=("build", "run"))
	depends_on("r-rfast", type=("build", "run"))
