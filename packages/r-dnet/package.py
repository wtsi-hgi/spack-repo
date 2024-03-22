# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class RDnet(RPackage):
    """The focus of the dnet by Fang and Gough (2014) <doi:10.1186/s13073-014-0064-8> is to make sense of omics data (such as gene expression and mutations) from different angles including: integration with molecular networks, enrichments using ontologies, and relevance to gene evolutionary ages. Integration is achieved to identify a gene subnetwork from the whole gene network whose nodes/genes are labelled with informative data (such as the significant levels of differential expression or survival risks). To help make sense of identified gene networks, enrichment analysis is also supported using a wide variety of pre-compiled ontologies and phylostratific gene age information in major organisms including: human, mouse, rat, chicken, C.elegans, fruit fly, zebrafish and arabidopsis. Add-on functionalities are supports for calculating semantic similarity between ontology terms (and between genes) and for calculating network affinity based on random walk; both can be done via high-performance parallel computing."""

    homepage = "https://web.archive.org/web/20231209215656/http://dnet.r-forge.r-project.org/"
    cran = "dnet"

    version("1.1.7", sha256="ac2be6d2b64dd6f63002c80b4646506fadf3ec9dc690249193db40d1d17db816")
    version("1.1.6", sha256="74daf37b54b041409a5f91890c6c077fd580236a8e04adaf4b8146c869c6fb87")
    version("1.1.5", sha256="e87c92e4d989a174836e48c24ecbb698973ebc7f619202a77c2321f034c9833f")
    version("1.1.4", sha256="a8d4f8541420fea78996633d4ca097ef433088eb5083e73a73a915a440598c75")
    version("1.1.3", sha256="5f9912db34f098fa53f12cd7701238a1b9f201ba46586afe8e415eb8d89a64ab")
    version("1.1.2", sha256="56fde3b39b3253889d2acd89fc6a9d483733ad577578782ed97df85c8a646178")
    version("1.1.1", sha256="d923a7d5679835293352e0999e7715d34c14f6ad92f2ed966f29446a500943de")
    version("1.0.10", sha256="2f0b7c00f2a30f67ecb9fa7cf9cea86ed9dfef7897205b6d8172c4a9f9c63904")
    version("1.0.9", sha256="6c423defb755e28b8a6ba1d33be818bcba33851070c3899dbf8e38d02d6b7c3f")
    version("1.0.8", sha256="821c3855f57e4beb8b6bac697e733116888a31b36f72adee826ccbf757bd7239")
    version("1.0.7", sha256="80440ae7d4adf02698f633e694c73f956e78aa5435de00c9b0aa875a8f274629")
    version("1.0.6", sha256="56060601031f5bb28c6bd70a8aec18329757d8e0f5cbbdde92dc419a9d171b7e")
    version("1.0.5", sha256="05aba1f69c93239a6c360ad285ff07b8874f2586ee77533dcc63d017c0497d8a")
    version("1.0.4", sha256="0e92c25673aeef68162bab80d77f315871e7010dcca98bbeafe99ebf02cb80f2")
    version("1.0.3", sha256="2faf24fbab67c8549fd362239b21bee9f697edab329fafbe44af43c042b49553")
    version("1.0.2", sha256="7688e67f47c905ff4fe344695f93fed8a7c59d88667a936eace0f2620a592184")
    version("1.0.1", sha256="9872bc0fee0af7b55ee575fa35b47c73134b9dbe31dd8de49efd1b0bbd901eee")
    version("1.0.0", sha256="3581d73a8008da2d247787d9a7bced8f76d7b19a4bf5eb262d9e666b721a5d88")
    version("0.99.0", sha256="09806f57465c9a1c413dd446ea7093ba0c581f6bce8a46c3ded384ad4034bbc0")

    depends_on("r@3.1:", type=("build", "run"))
    depends_on("r-igraph", type=("build", "run"))
    depends_on("r-suprahex", type=("build", "run"))
    depends_on("r-graph", type=("build", "run"))
    depends_on("r-rgraphviz", type=("build", "run"))
    depends_on("r-matrix", type=("build", "run"))
