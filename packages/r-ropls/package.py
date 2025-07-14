# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRopls(RPackage):
	"""PCA, PLS(-DA) and OPLS(-DA) for multivariate analysis and feature selection of omics data

	Latent variable modeling with Principal Component Analysis (PCA) and Partial Least Squares (PLS) are powerful methods for visualization, regression, classification, and feature selection of omics data where the number of variables exceeds the number of samples and with multicollinearity among variables. Orthogonal Partial Least Squares (OPLS) enables to separately model the variation correlated (predictive) to the factor of interest and the uncorrelated (orthogonal) variation. While performing similarly to PLS, OPLS facilitates interpretation. Successful applications of these chemometrics techniques include spectroscopic data such as Raman spectroscopy, nuclear magnetic resonance (NMR), mass spectrometry (MS) in metabolomics and proteomics, but also transcriptomics data. In addition to scores, loadings and weights plots, the package provides metrics and graphics to determine the optimal number of components (e.g. with the R2 and Q2 coefficients), check the validity of the model by permutation testing, detect outliers, and perform feature selection (e.g. with Variable Importance in Projection or regression coefficients). The package can be accessed via a user interface on the Workflow4Metabolomics.org online resource for computational metabolomics (built upon the Galaxy environment).
	"""
	
	homepage = "https://doi.org/10.1021/acs.jproteome.5b00354"
	bioc = "ropls"

	version("1.40.0", commit="4c98856d048ae6e10ee55f21cf41b1a44c839477")
	version("1.34.0", commit="415d359e77e6de80d23c57bfbd5ff86e9f439338")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-multiassayexperiment", type=("build", "run"))
	depends_on("r-multidataset", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
