# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RScmageck(RPackage):
    """A computational model to identify genes associated with multiple expression phenotypes from CRISPR screening coupled with single-cell RNA sequencing data.."""

    homepage = "https://bitbucket.org/weililab/scmageck/"
    url = "https://bitbucket.org/weililab/scmageck/downloads/scMAGeCK_1.9.2.tar.gz"

    version(
        "1.9.2",
        sha256="0350876eb634067e69c7516bf96eeebee7fb978470dc2d3ff410bd9b5c5ab870",
    )
    version(
        "1.5.1",
        sha256="bba0c033257bead1fbc9a3fd96beea41b01330b701562db5fd2e7bb4c8cf54e9",
    )
    version(
        "1.5.0",
        sha256="0d4169c204a0367c8b5f7f94eda2468d5079f0937cd7b24d68af5188acf03337",
    )
    version(
        "0.99.15",
        sha256="e05a2de3ec40617df4d84302647ef2571897704535f5973dc1f21ca99a3a84dd",
    )
    version(
        "0.99.13",
        sha256="0e7ffef2524d4ac711155c6a83d540cdb13221eec96a7fbc040ad9ecd6c7b141",
    )
    version(
        "0.99.12",
        sha256="9d3c2fa9692c4d79068ffa66e3e3c30056b9c0f0a2552b15a6a7e50b06e6ae08",
    )

    depends_on("r-seurat", type=("build", "run"))
    depends_on("r-ggplot2", type=("build", "run"))
    depends_on("r-rcpp", type=("build", "run"))
    depends_on("py-mageck@:1.5.1", type="run")
    depends_on("py-pysam", type="run")
