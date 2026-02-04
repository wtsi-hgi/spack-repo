# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSeurat(RPackage):
	"""Tools for Single Cell Genomics.

	A toolkit for quality control, analysis, and exploration of single cell RNA
	sequencing data. 'Seurat' aims to enable users to identify and interpret
	sources of heterogeneity from single cell transcriptomic measurements, and
	to integrate diverse types of single cell data. See Satija R, Farrell J,
	Gennert D, et al (2015) <doi:10.1038/nbt.3192>, Macosko E, Basu A, Satija
	R, et al (2015) <doi:10.1016/j.cell.2015.05.002>, and Stuart T, Butler A,
	et al (2019) <doi:10.1016/j.cell.2019.05.031> for more details."""

	license("MIT")

	cran = "Seurat"
	version("5.4.0", sha256="d200da7cb19a2fa4ead7ea4aa1bb703dbc59c594f01cb91c996ad862ad6f6417")
	version("5.3.1", sha256="354acba93ccef2d89f0780d14e3122f4093cb0379e7229a834b2afa6b82db223")
	version("5.3.0", sha256="12abaf6cea4aa30f73028387e74ecb405b17acbae414d43522e764f3179908a7")
	version("5.2.1", sha256="0e99c0f9a6fee4a1e5e241aa2f8bb82288ff08185680f283124854a7b22fda19")
	version("5.2.0", sha256="5b4935ef75c77408e92d1dad0b77f29630e3d910aff30b343c1c1b89d554405f")
	version("5.1.0", sha256="adcfb43d7a8cc55eaa7a0954a082ac95e14059a82901913379bfec115e224d59")
	version("5.0.3", md5="2112a71f0ea07db422650c86aacc5d25")
	version("5.0.2", sha256="acbcef1706590bee0f2f88c49b7f9bdaff3aed6f24a23ceda601dd086b5289b4")
	version("5.0.1", md5="3965b1ee0bdc7f005d250a3dd429bcc3")
	version("5.0.0", sha256="bb8c91610f58753aa57f38bf2ef1c97c9c85fbfe89c1c47a33805f3eb5eb78c3")
	version("4.4.0", sha256="0f17df9597642cfc1db4d8718f0b59ebab9fbed328b1f885f42ee85ea0dcb4dd")
	version("4.3.0", sha256="7ebacb3b86f74279de60b597f9a6e728f0668719811b0dca3425d21762fff97c")
	version("4.2.1", sha256="410238b6ca147451b43800a6e49c132fa5f6aacfe6b93b39a1e4d61257a9e35e")
	version("4.2.0", sha256="22a3d22a9ba255c4db5b37339b183fdfb91e2d37a8b8d58a9ff45b1bc414ebef")
	version("4.1.1", sha256="201aa96919b32378fc4cb67557188214c1242dcbae50cadd7d12c86666af8ace")
	version("4.1.0", sha256="2505829a2763e449684dd1b107ee6982e019ee9fecb093adca7b283cad1b315d")
	version("3.2.3", sha256="83aa48f75c3756bee23e108a8b01028366e24f237fe990cb441f3525e0613f87")
	version("3.1.0", sha256="d8d3fad2950a8f791376e3d20c72ea07c68bf8d82d800661cab5ce696db39d45")
	version("3.0.2", sha256="16df5dec6b41d49320c5bf5ce30eb3b7dedeea69b054b55b77528f2f2b7bce04")
	version("3.0.1", sha256="8c467bdbfdb9aff51bde6a897ff98a7389941f688639d8f1d36c71dde076a257")
	version("2.1.0", sha256="7d20d231b979a4aa63cd7dae7e725405212e8975889f12b8d779c6c896c10ac3")
	version("2.0.1", sha256="6aa33aa3afb29a8be364ab083c7071cfbc56ad042a019bcf6f939e0c8c7744f0")

	depends_on("r@4:", type=("build", "run"))
	# Seurat depends on different SeuratObject majors across versions
	depends_on("r-seuratobject@4:", type=("build", "run"), when="@4:")
	depends_on("r-seuratobject@5:", type=("build", "run"), when="@5:")
	depends_on("r-seuratobject@5.0.2:", type=("build", "run"), when="@5.3.0:")
	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-cowplot", type=("build", "run"))
	depends_on("r-fastdummies", type=("build", "run"))
	depends_on("r-fitdistrplus", type=("build", "run"))
	depends_on("r-future", type=("build", "run"))
	depends_on("r-future-apply", type=("build", "run"))
	# Seurat imports foreach for parallel processing constructs
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-generics@0.1.3:", type=("build", "run"))
	depends_on("r-ggplot2@3.3:", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("r-ggridges", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-ica", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-irlba", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-kernsmooth", type=("build", "run"))
	depends_on("r-leiden@0.3.1:", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-lmtest", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-matrix@1.5.0:", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-miniui", type=("build", "run"))
	depends_on("r-patchwork", type=("build", "run"))
	depends_on("r-pbapply", type=("build", "run"))
	depends_on("r-plotly@4.9:", type=("build", "run"))
	depends_on("r-png", type=("build", "run"))
	depends_on("r-progressr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rann", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-rcpp@0.11:", type=("build", "run"))
	depends_on("r-rcppannoy@0.0.18:", type=("build", "run"))
	depends_on("r-rcpphnsw", type=("build", "run"))
	depends_on("r-reticulate", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-rocr", type=("build", "run"))
	depends_on("r-rspectra", type=("build", "run"))
	depends_on("r-rtsne", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-scattermore@1.2:", type=("build", "run"))
	depends_on("r-sctransform@0.4.1:", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-spatstat-explore", type=("build", "run"))
	depends_on("r-spatstat-geom", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-uwot@0.1.10:", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
	depends_on("r-rcppprogress", type=("build", "run"))
	depends_on("r-spatstat-core", type=("build", "run"), when="@:4.1.1")
	depends_on("r-leidenbase", type=("build", "run"), when="@5.3.0:")
