# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REscher(RPackage):
	"""Unified multi-dimensional visualizations with Gestalt principles

	The creation of effective visualizations is a fundamental component of data analysis. In biomedical research, new challenges are emerging to visualize multi-dimensional data in a 2D space, but current data visualization tools have limited capabilities. To address this problem, we leverage Gestalt principles to improve the design and interpretability of multi-dimensional data in 2D data visualizations, layering aesthetics to display multiple variables. The proposed visualization can be applied to spatially-resolved transcriptomics data, but also broadly to data visualized in 2D space, such as embedding visualizations. We provide this open source R package escheR, which is built off of the state-of-the-art ggplot2 visualization framework and can be seamlessly integrated into genomics toolboxes and workflows.
	"""
	
	homepage = "https://github.com/boyiguo1/escheR"
	bioc = "escheR" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/escheR_1.2.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/escheR/escheR_1.2.0.tar.gz"]

	version("1.8.0", tag="RELEASE_3_21")
	version("1.2.0", sha256="d997b24d8123ce01826c65f7aa09dacd50869d5d3597679dbffc1416da9c6141")

	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r@4.3:", type=("build", "run"))
	depends_on("r-spatialexperiment@1.6.1:", type=("build", "run"))
	depends_on("r-singlecellexperiment", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
