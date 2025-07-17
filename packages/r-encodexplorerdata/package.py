# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REncodexplorerdata(RPackage):
    """A compilation of ENCODE metadata

    This package allows user to quickly access ENCODE project files metadata and give access to helper functions to query the ENCODE rest api, download ENCODE datasets and save the database in SQLite format.
    """

    bioc = "ENCODExplorerData"

    version("0.99.5", commit="c69d7b99ec8cfe1fdb85f520877ed68ce7453074")
    version("0.99.5", commit="c69d7b99ec8cfe1fdb85f520877ed68ce7453074")

    depends_on("r@3.6:", type=("build", "run"))
    depends_on("r-jsonlite", type=("build", "run"))
    depends_on("r-rcurl", type=("build", "run"))
    depends_on("r-data-table", type=("build", "run"))
