# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMygene(RPackage):
    """Access MyGene.Info_ services

    MyGene.Info_ provides simple-to-use REST web services to query/retrieve gene annotation data. It's designed with simplicity and performance emphasized. *mygene*, is an easy-to-use R wrapper to access MyGene.Info_ services.
    """

    bioc = "mygene"

    version("1.44.0", commit="29b599e0a83e8dc84283fd683951c7ee00d90b11")
    version("1.38.0", commit="f4ab79163c31e10016eaff549d051e350b6fb1d2")

    depends_on("r@3.2.1:", type=("build", "run"))
    depends_on("r-genomicfeatures", type=("build", "run"))
    depends_on("r-httr@0.3:", type=("build", "run"))
    depends_on("r-jsonlite@0.9.7:", type=("build", "run"))
    depends_on("r-s4vectors", type=("build", "run"))
    depends_on("r-hmisc", type=("build", "run"))
    depends_on("r-sqldf", type=("build", "run"))
    depends_on("r-plyr", type=("build", "run"))
