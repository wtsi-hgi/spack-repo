# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDensvis(RPackage):
	"""Density-Preserving Data Visualization via Non-Linear Dimensionality
	Reduction.

	Implements the density-preserving modification to t-SNE and UMAP described
	by Narayan et al. (2020) . The non-linear dimensionality reduction
	techniques t-SNE and UMAP enable users to summarise complex
	high-dimensional sequencing data such as single cell RNAseq using lower
	dimensional representations. These lower dimensional representations enable
	the visualisation of discrete transcriptional states, as well as continuous
	trajectory (for example, in early development). However, these methods
	focus on the local neighbourhood structure of the data. In some cases, this
	results in misleading visualisations, where the density of cells in the
	low-dimensional embedding does not represent the transcriptional
	heterogeneity of data in the original high-dimensional space. den-SNE and
	densMAP aim to enable more accurate visual interpretation of
	high-dimensional datasets by producing lower-dimensional embeddings that
	accurately represent the heterogeneity of the original high-dimensional
	space, enabling the identification of homogeneous and heterogeneous cell
	states. This accuracy is accomplished by including in the optimisation
	process a term which considers the local density of points in the original
	high-dimensional space. This can help to create visualisations that are
	more representative of heterogeneity in the original high-dimensional
	space."""

	bioc = "densvis"
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/densvis_1.12.1.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/densvis/densvis_1.12.1.tar.gz"]
	version("1.10.0", commit="833db1fb7b2a5667575cc2e7c2fefc8360c8d7fb")
	version("1.12.1", md5="ca37ec5b6c247bc5b20194bd889579e0")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-basilisk", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-reticulate", type=("build", "run"))
	depends_on("r-rtsne", type=("build", "run"))
	depends_on("r-irlba", type=("build", "run"))
