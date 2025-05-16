# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHdwgcna(RPackage):
    """High dimensional weighted gene co-expression network analysis (hdWGCNA)
    for single-cell RNA-seq or spatial transcriptomics. hdWGCNA identifies
    modules of highly co-expressed genes and provides context for these modules
    via statistical testing and biological knowledge sources."""

    homepage = "https://github.com/smorabit/hdWGCNA"
    url = "https://github.com/smorabit/hdWGCNA/archive/refs/tags/v0.3.0.tar.gz"
    git = "https://github.com/smorabit/hdWGCNA.git"

    version("0.4.05", commit="2b9df2f26339fc1e86f7223508261fb1d61001d9")
    version("0.3.00", sha256="5ef9980f6d25b41af17ebad76722766db72fb8162d5ae7af4565893d26c9ed1f")

    depends_on("r-harmony", type=("build", "run"))
    depends_on("r-seurat", type=("build", "run"))
    depends_on("r-ggrepel", type=("build", "run"))
    depends_on("r-wgcna", type=("build", "run"))
    depends_on("r-igraph", type=("build", "run"))
    depends_on("r-matrix", type=("build", "run"))
    depends_on("r-ggplot2", type=("build", "run"))
    depends_on("r-dplyr", type=("build", "run"))
    depends_on("r-tester", type=("build", "run"))
    depends_on("r-proxy", type=("build", "run"))
    depends_on("r-ggraph", type=("build", "run"))
    depends_on("r-tidygraph", type=("build", "run"))
    depends_on("r-ucell", type=("build", "run"))
    depends_on("r-geneoverlap", type=("build", "run"))
    depends_on("r-genomicranges", type=("build", "run"))
    depends_on("r-enrichr", type=("build", "run"))
