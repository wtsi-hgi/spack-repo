# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSingler(RPackage):
    """Reference-Based Single-Cell RNA-Seq Annotation

    Performs unbiased cell type recognition from single-cell RNA sequencing data, by leveraging reference transcriptomic datasets of pure cell types to infer the cell of origin of each single cell independently.
    """

    homepage = "https://github.com/LTLA/SingleR"
    bioc = "SingleR"

    version("2.10.0", commit="2c586f6c4e5de5c8bf8fdac1bbeca9d4d090e6c8")
    version("2.4.1", commit="fab56fd58ebfbecd9c97158aebd40ea46000ffb6")

    depends_on("r-summarizedexperiment", type=("build", "run"))
    depends_on("r-matrix", type=("build", "run"))
    depends_on("r-s4vectors", type=("build", "run"))
    depends_on("r-delayedarray", type=("build", "run"))
    depends_on("r-delayedarray@0.8.0:", type=("build", "run"), when="@2.10:")
    depends_on("r-delayedmatrixstats", type=("build", "run"))
    depends_on("r-delayedmatrixstats@1.30.0:", type=("build", "run"), when="@2.10:")
    depends_on("r-biocparallel", type=("build", "run"))
    depends_on("r-biocsingular", type=("build", "run"))
    depends_on("r-biocsingular@1.24.0:", type=("build", "run"), when="@2.10:")
    depends_on("r-rcpp", type=("build", "run"))
    depends_on("r-assorthead", type=("build", "run"), when="@2.10:")
    depends_on("r-beachmat", type=("build", "run"))
    depends_on("r-beachmat@2.23.5:", type=("build", "run"), when="@2.10:")
    depends_on("r-biocneighbors", type=("build", "run"))
    depends_on("r-biocneighbors@2.2.0:", type=("build", "run"), when="@2.10:")
