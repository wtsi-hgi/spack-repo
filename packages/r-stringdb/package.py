# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStringdb(RPackage):
    """STRINGdb - Protein-Protein Interaction Networks and Functional Enrichment Analysis

    The STRINGdb package provides a R interface to the STRING protein-protein interactions database (https://string-db.org).
    """

    bioc = "STRINGdb"

    version("2.20.0", commit="d33cf9b66326584e58c954c07484908e0a430719")
    version("2.14.3", commit="18a4da8d92743b7facf418bd27701d9cfba244fe")
    version("2.14.0", md5="6dc5819519574f0656e4b811e4618db7")

    depends_on("r@2.14:", type=("build", "run"))
    depends_on("r-png", type=("build", "run"))
    depends_on("r-sqldf", type=("build", "run"))
    depends_on("r-plyr", type=("build", "run"))
    depends_on("r-igraph", type=("build", "run"))
    depends_on("r-httr", type=("build", "run"))
    depends_on("r-rcolorbrewer", type=("build", "run"))
    depends_on("r-gplots", type=("build", "run"))
    depends_on("r-hash", type=("build", "run"))
    depends_on("r-plotrix", type=("build", "run"))
