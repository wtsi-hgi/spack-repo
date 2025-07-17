# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTxdbAthalianaBiomartPlantsmart25(RPackage):
    """Annotation package for TxDb object(s)

    Exposes an annotation databases generated from BioMart by exposing these as TxDb objects
    """

    bioc = "TxDb.Athaliana.BioMart.plantsmart25"
    urls = [
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/TxDb.Athaliana.BioMart.plantsmart25_3.1.3.tar.gz",
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/TxDb.Athaliana.BioMart.plantsmart25/TxDb.Athaliana.BioMart.plantsmart25_3.1.3.tar.gz",
    ]

    version(
        "3.1.3",
        sha256="a3ee0b146d31b6addaa2362789b128e5d94edbef0dcd11b58ff58f700d05db28",
        url="https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/TxDb.Athaliana.BioMart.plantsmart25_3.1.3.tar.gz",
    )

    depends_on("r-genomicfeatures", type=("build", "run"))
    depends_on("r-annotationdbi", type=("build", "run"))
