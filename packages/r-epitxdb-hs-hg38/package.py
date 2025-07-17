# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REpitxdbHsHg38(RPackage):
    """Annotation package for EpiTxDb objects

    Exposes an annotation databases generated from several sources by exposing these as EpiTxDb object. Generated for Homo sapiens/hg38.
    """

    homepage = "https://github.com/FelixErnst/EpiTxDb.Hs.hg38"
    bioc = "EpiTxDb.Hs.hg38"

    version("0.99.7", commit="135951cd4723a6ac6b21b56b1445622d005e8dad")
    version("0.99.7", commit="135951cd4723a6ac6b21b56b1445622d005e8dad")

    depends_on("r@4:", type=("build", "run"))
    depends_on("r-annotationhub", type=("build", "run"))
    depends_on("r-epitxdb", type=("build", "run"))
