# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBiodbhmdb(RPackage):
    """biodbHmdb, a library for connecting to the HMDB Database

    The biodbHmdb library is an extension of the biodb framework package that provides access to the HMDB Metabolites database. It allows to download the whole HMDB Metabolites database locally, access entries and search for entries by name or description. A future version of this package will also include a search by mass and mass spectra annotation.
    """

    homepage = "https://github.com/pkrog/biodbHmdb"
    bioc = "biodbHmdb"

    version("1.14.0", commit="a7f0a0f2cfdd2dbddbb598d7fafd909bf0951dfe")
    version("1.8.0", commit="0efcfbf27d91da65c98a87040d16b22d10a665fe")

    depends_on("r@4.1:", type=("build", "run"))
    depends_on("r-r6", type=("build", "run"))
    depends_on("r-biodb@1.3.2:", type=("build", "run"))
    depends_on("r-rcpp", type=("build", "run"))
    depends_on("r-zip", type=("build", "run"))
    depends_on("r-testthat", type=("build", "run"))
