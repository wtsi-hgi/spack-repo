# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVelociraptor(RPackage):
    """Toolkit for Single-Cell Velocity

    This package provides Bioconductor-friendly wrappers for RNA velocity calculations in single-cell RNA-seq data. We use the basilisk package to manage Conda environments, and the zellkonverter package to convert data structures between SingleCellExperiment (R) and AnnData (Python). The information produced by the velocity methods is stored in the various components of the SingleCellExperiment class.
    """

    homepage = "https://github.com/kevinrue/velociraptor"
    bioc = "velociraptor"

    version("1.18.0", commit="b2c6328b6062dc91d14eb24f7a5b1fb30d344603")
    version("1.12.0", commit="05c6c2a3babbf63c0d3349bec22fa0ecceb38af8")

    depends_on("r-summarizedexperiment", type=("build", "run"))
    depends_on("r-matrix", type=("build", "run"))
    depends_on("r-biocgenerics", type=("build", "run"))
    depends_on("r-reticulate", type=("build", "run"))
    depends_on("r-s4vectors", type=("build", "run"))
    depends_on("r-delayedarray", type=("build", "run"))
    depends_on("r-basilisk", type=("build", "run"))
    depends_on("r-zellkonverter", type=("build", "run"))
    depends_on("r-scuttle", type=("build", "run"))
    depends_on("r-singlecellexperiment", type=("build", "run"))
    depends_on("r-biocparallel", type=("build", "run"))
    depends_on("r-biocsingular", type=("build", "run"))
