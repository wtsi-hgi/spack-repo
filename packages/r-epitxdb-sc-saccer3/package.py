# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REpitxdbScSaccer3(RPackage):
    """Annotation package for EpiTxDb objects

    Exposes an annotation databases generated from several sources by exposing these as EpiTxDb object. Generated for Saccharomyces cerevisiae/sacCer3.
    """

    homepage = "https://github.com/FelixErnst/EpiTxDb.Sc.sacCer3"
    bioc = "EpiTxDb.Sc.sacCer3"

    version("0.99.5", commit="bf65d31fcb72328a561ef75674612c0ce1e73395")
    version("0.99.5", commit="bf65d31fcb72328a561ef75674612c0ce1e73395")

    depends_on("r@4:", type=("build", "run"))
    depends_on("r-annotationhub", type=("build", "run"))
    depends_on("r-epitxdb", type=("build", "run"))
