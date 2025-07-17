# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHeatplus(RPackage):
    """Heatmaps with row and/or column covariates and colored clusters

    Display a rectangular heatmap (intensity plot) of a data matrix. By default, both samples (columns) and features (row) of the matrix are sorted according to a hierarchical clustering, and the corresponding dendrogram is plotted. Optionally, panels with additional information about samples and features can be added to the plot.
    """

    homepage = "https://github.com/alexploner/Heatplus"
    bioc = "Heatplus"

    version("3.16.0", commit="2bba861c6e17d8f78b014514df5c33c4281f23c2")
    version("3.10.0", commit="2b3a0fc54ccecc4b60188df349378bd9e8f83dc8")

    depends_on("r-rcolorbrewer", type=("build", "run"))
