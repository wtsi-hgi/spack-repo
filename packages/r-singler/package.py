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
    urls = [
        "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/SingleR_2.4.1.tar.gz",
        "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/SingleR/SingleR_2.4.1.tar.gz",
    ]

    version("2.10.0", tag="RELEASE_3_21")
    version("2.4.1", sha256="4d8fb557544732511d3ae2e25959fb3f53c6756b2da5db6f2cce69155b219b7e")

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
