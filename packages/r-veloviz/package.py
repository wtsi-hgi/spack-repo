# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVeloviz(RPackage):
    """VeloViz: RNA-velocity informed 2D embeddings for visualizing cell state trajectories

    VeloViz uses each cell’s current observed and predicted future transcriptional states inferred from RNA velocity analysis to build a nearest neighbor graph between cells in the population. Edges are then pruned based on a cosine correlation threshold and/or a distance threshold and the resulting graph is visualized using a force-directed graph layout algorithm. VeloViz can help ensure that relationships between cell states are reflected in the 2D embedding, allowing for more reliable representation of underlying cellular trajectories.
    """

    bioc = "veloviz"

    version("1.14.0", commit="24284741d46e7d75d4d77c759475ffeff24583e3")
    version("1.8.0", commit="e9aec2c2f7ed4bc3404d2ce7d27329ab0f123c37")

    depends_on("r@4.1:", type=("build", "run"))
    depends_on("r-rcpp", type=("build", "run"))
    depends_on("r-matrix", type=("build", "run"))
    depends_on("r-igraph", type=("build", "run"))
    depends_on("r-mgcv", type=("build", "run"))
    depends_on("r-rspectra", type=("build", "run"))
