# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMacsquantifyr(RPackage):
    """Fast treatment of MACSQuantify FACS data

    Automatically process the metadata of MACSQuantify FACS sorter. It runs multiple modules: i) imports of raw file and graphical selection of duplicates in well plate, ii) computes statistics on data and iii) can compute combination index.
    """

    bioc = "MACSQuantifyR"

    version("1.22.0", commit="569537261a80c5a7fc3b86ab06dc8b4bd6f01cc7")
    version("1.16.0", commit="4ddabf78bdf754d66da8d6d7b0266fba78bc20cc")

    depends_on("r-readxl", type=("build", "run"))
    depends_on("r-ggplot2", type=("build", "run"))
    depends_on("r-ggrepel", type=("build", "run"))
    depends_on("r-latticeextra", type=("build", "run"))
    depends_on("r-lattice", type=("build", "run"))
    depends_on("r-rmarkdown", type=("build", "run"))
    depends_on("r-png", type=("build", "run"))
    depends_on("r-gridextra", type=("build", "run"))
    depends_on("r-prettydoc", type=("build", "run"))
    depends_on("r-rvest", type=("build", "run"))
    depends_on("r-xml2", type=("build", "run"))
