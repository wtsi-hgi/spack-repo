# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCellmapperdata(RPackage):
    """Pre-processed data for use with the CellMapper package

    Experiment data package. Contains microarray data from several large expression compendia that have been pre-processed for use with the CellMapper package. This pre-processed data is recommended for routine searches using the CellMapper package.
    """

    bioc = "CellMapperData"

    version("1.34.0", commit="e0581fb367d53a7462e387aba5b625477e52df1a")
    version("1.28.0", commit="7a0e00b0d6772d8d887eaff04e09a5576c9a485f")

    depends_on("r-experimenthub", type=("build", "run"))
    depends_on("r-cellmapper", type=("build", "run"))
