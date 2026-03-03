# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class RBoldconnectr(RPackage):
    """BOLDconnectR is a package designed for retrieval, transformation and analysis of the data available in the Barcode Of Life Data Systems (BOLD) database. This package provides the functionality to obtain public and private user data available in the database in the Barcode Core Data Model (BCDM) format. Data include information on the taxonomy,geography,collection,identification and DNA barcode sequence of every submission."""

    homepage = ""
    git = "https://github.com/boldsystems-central/BOLDconnectR.git"

    version("2025-01-14", commit="62b32fe53149f047c7fb7530040cd2c74a48d1cc")

    depends_on("r-ape@5.5:", type=("build", "run"))
    depends_on("r-bat@2.0:", type=("build", "run"))
    depends_on("r-data-table@1.13:", type=("build", "run"))
    depends_on("r-dplyr@1.0.1:", type=("build", "run"))
    depends_on("r-ggplot2@3.3.2:", type=("build", "run"))
    depends_on("r-httr@1.4.2:", type=("build", "run"))
    depends_on("r-jsonlite@1.7:", type=("build", "run"))
    depends_on("r-maps@3.3:", type=("build", "run"))
    depends_on("r-reshape2", type=("build", "run"))
    depends_on("r-rnaturalearth", type=("build", "run"))
    depends_on("r-sf@0.9.4:", type=("build", "run"))
    depends_on("r-skimr@2.1.2:", type=("build", "run"))
    depends_on("r-tidyr@1.1.1:", type=("build", "run"))
    depends_on("r-vegan@2.5.7:", type=("build", "run"))
