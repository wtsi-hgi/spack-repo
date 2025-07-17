# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTxdbAthalianaBiomartPlantsmart28(RPackage):
    """Annotation package for TxDb object(s)

    Exposes an annotation databases generated from BioMart by exposing these as TxDb objects
    """

    bioc = "TxDb.Athaliana.BioMart.plantsmart28"
    urls = [
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/TxDb.Athaliana.BioMart.plantsmart28_3.2.2.tar.gz",
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/TxDb.Athaliana.BioMart.plantsmart28/TxDb.Athaliana.BioMart.plantsmart28_3.2.2.tar.gz",
    ]

    version(
        "3.2.2",
        sha256="391aac80e3055875639103dd117be1f8d98b1ccd628d872911c097d257de5efa",
        url="https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/TxDb.Athaliana.BioMart.plantsmart28_3.2.2.tar.gz",
    )

    depends_on("r-genomicfeatures@1.21.30:", type=("build", "run"))
    depends_on("r-annotationdbi", type=("build", "run"))
