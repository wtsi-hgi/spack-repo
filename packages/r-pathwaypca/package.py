# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPathwaypca(RPackage):
	"""Integrative Pathway Analysis with Modern PCA Methodology and Gene Selection

	pathwayPCA is an integrative analysis tool that implements the principal component analysis (PCA) based pathway analysis approaches described in Chen et al. (2008), Chen et al. (2010), and Chen (2011). pathwayPCA allows users to: (1) Test pathway association with binary, continuous, or survival phenotypes. (2) Extract relevant genes in the pathways using the SuperPCA and AES-PCA approaches. (3) Compute principal components (PCs) based on the selected genes. These estimated latent variables represent pathway activities for individual subjects, which can then be used to perform integrative pathway analysis, such as multi-omics analysis. (4) Extract relevant genes that drive pathway significance as well as data corresponding to these relevant genes for additional in-depth analysis. (5) Perform analyses with enhanced computational efficiency with parallel computing and enhanced data safety with S4-class data objects. (6) Analyze studies with complex experimental designs, with multiple covariates, and with interaction effects, e.g., testing whether pathway association with clinical phenotype is different between male and female subjects. Citations: Chen et al. (2008) <https://doi.org/10.1093/bioinformatics/btn458>; Chen et al. (2010) <https://doi.org/10.1002/gepi.20532>; and Chen (2011) <https://doi.org/10.2202/1544-6115.1697>.
	"""
	
	homepage = "<https://gabrielodom.github.io/pathwayPCA/>"
	bioc = "pathwayPCA" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/pathwayPCA_1.18.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/pathwayPCA/pathwayPCA_1.18.0.tar.gz"]

	version("1.24.0", tag="RELEASE_3_21")
	version("1.18.0", sha256="e4524ffdd297f9c0417c972125b05770c790bd92d83ee89f31a675ee9655a091")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-lars", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
