# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTxdbRnorvegicusBiomartIgis(RPackage):
    """Annotation package for TxDb object(s)

    Exposes an annotation databases generated from BioMart by exposing these as TxDb objects
    """

    bioc = "TxDb.Rnorvegicus.BioMart.igis"
    urls = [
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/TxDb.Rnorvegicus.BioMart.igis_2.3.2.tar.gz",
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/TxDb.Rnorvegicus.BioMart.igis/TxDb.Rnorvegicus.BioMart.igis_2.3.2.tar.gz",
    ]

    version(
        "2.3.2",
        sha256="e6502a4d3dae677bffebb80a24b8b6084859470d3754dde55b9d8e87e6dc2981",
    )

    depends_on("r-genomicfeatures", type=("build", "run"))
    depends_on("r-annotationdbi", type=("build", "run"))
