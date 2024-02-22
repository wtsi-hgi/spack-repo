# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMwastools(RPackage):
	"""MWASTools: an integrated pipeline to perform metabolome-wide association studies

	MWASTools provides a complete pipeline to perform metabolome-wide association studies. Key functionalities of the package include: quality control analysis of metabonomic data; MWAS using different association models (partial correlations; generalized linear models); model validation using non-parametric bootstrapping; visualization of MWAS results; NMR metabolite identification using STOCSY; and biological interpretation of MWAS results.
	"""
	
	bioc = "MWASTools" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/MWASTools_1.26.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/MWASTools/MWASTools_1.26.0.tar.gz"]

	version("1.26.0", md5="4af3f3512a794c7944a27bfad640aa81")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-glm2", type=("build", "run"))
	depends_on("r-ppcor", type=("build", "run"))
	depends_on("r-qvalue", type=("build", "run"))
	depends_on("r-car", type=("build", "run"))
	depends_on("r-boot", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-kegggraph", type=("build", "run"))
	depends_on("r-rcurl", type=("build", "run"))
	depends_on("r-keggrest", type=("build", "run"))
	depends_on("r-complexheatmap", type=("build", "run"))
