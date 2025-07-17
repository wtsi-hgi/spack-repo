# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBiodbchebi(RPackage):
    """biodbChebi, a library for connecting to the ChEBI Database

    The biodbChebi library provides access to the ChEBI Database, using biodb package framework. It allows to retrieve entries by their accession number. Web services can be accessed for searching the database by name, mass or other fields.
    """

    homepage = "https://github.com/pkrog/biodbChebi"
    bioc = "biodbChebi"

    version("1.14.0", commit="b8d718f4c261df352beea23b89477134d024312b")
    version("1.8.0", commit="664af9c7d996799db030684217c5acc81eb9d3b3")

    depends_on("r@4.1:", type=("build", "run"))
    depends_on("r-r6", type=("build", "run"))
    depends_on("r-biodb@1.1.5:", type=("build", "run"))
