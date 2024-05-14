# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class RHdwgcna(RPackage):
    """FIXME: Put a proper description of your package here."""

    homepage = "https://www.example.com"
    url = "https://github.com/smorabit/hdWGCNA/archive/refs/tags/v0.3.00.tar.gz"

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
