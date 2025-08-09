# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpatialfeatureexperiment(RPackage):
    """Integrating SpatialExperiment with Simple Features in sf

    A new S4 class integrating Simple Features with the R package sf to bring geospatial data analysis methods based on vector data to spatial transcriptomics. Also implements management of spatial neighborhood graphs and geometric operations. This pakage builds upon SpatialExperiment and SingleCellExperiment, hence methods for these parent classes can still be used.
    """

    homepage = "https://github.com/pachterlab/SpatialFeatureExperiment"
    bioc = "SpatialFeatureExperiment"

    version("1.10.1", commit="0098d4373b2fa1b5315157d621250092543fe211")
    version("1.4.0", commit="13f2a6b4db97e177e789cf75fd995c7d3a324057")

    depends_on("r@4.2:", type=("build", "run"))
    # Additional runtime dependencies surfaced during install on R 4.4
    depends_on("r-data-table", type=("build", "run"))
    depends_on("r-dropletutils", type=("build", "run"))
    depends_on("r-ebimage", type=("build", "run"))
    depends_on("r-sfheaders", type=("build", "run"))
    depends_on("r-spatialreg", type=("build", "run"))
    depends_on("r-zeallot", type=("build", "run"))
    depends_on("r-biocgenerics", type=("build", "run"))
    depends_on("r-biocneighbors", type=("build", "run"))
    depends_on("r-biocparallel", type=("build", "run"))
    depends_on("r-matrix", type=("build", "run"))
    depends_on("r-rjson", type=("build", "run"))
    depends_on("r-rlang", type=("build", "run"))
    depends_on("r-s4vectors", type=("build", "run"))
    depends_on("r-sf", type=("build", "run"))
    depends_on("r-singlecellexperiment", type=("build", "run"))
    depends_on("r-spatialexperiment", type=("build", "run"))
    depends_on("r-spdep@1.1.7:", type=("build", "run"))
    depends_on("r-summarizedexperiment", type=("build", "run"))
    depends_on("r-terra", type=("build", "run"))
