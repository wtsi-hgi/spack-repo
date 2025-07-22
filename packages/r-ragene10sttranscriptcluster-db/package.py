# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRagene10sttranscriptclusterDb(RPackage):
    """Affymetrix ragene10 annotation data (chip ragene10sttranscriptcluster)

    Affymetrix ragene10 annotation data (chip ragene10sttranscriptcluster) assembled using data from public repositories
    """

    bioc = "ragene10sttranscriptcluster.db"
    urls = [
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/ragene10sttranscriptcluster.db_8.8.0.tar.gz",
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/ragene10sttranscriptcluster.db/ragene10sttranscriptcluster.db_8.8.0.tar.gz",
    ]

    version(
        "8.8.0",
        sha256="3e31acf0a2fc8fd65a0334e521f4c41066b2bc9ac031fc2b4c920b16ff8768c7",
    )

    depends_on("r@2.7:", type=("build", "run"))
    depends_on("r-annotationdbi", type=("build", "run"))
    depends_on("r-org-rn-eg-db@3.13:", type=("build", "run"))
