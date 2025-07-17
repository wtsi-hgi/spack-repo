# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTrnadbimport(RPackage):
    """Importing from tRNAdb and mitotRNAdb as GRanges objects

    tRNAdbImport imports the entries of the tRNAdb and mtRNAdb (http://trna.bioinf.uni-leipzig.de) as GRanges object.
    """

    bioc = "tRNAdbImport"

    version("1.26.0", commit="2c327ce9d57fad5d7a76576a9809502de6057e87")
    version("1.20.1", commit="c5a12a3b92b5f59a307f5cd522e2c64821541b98")

    depends_on("r@3.6:", type=("build", "run"))
    depends_on("r-genomicranges", type=("build", "run"))
    depends_on("r-modstrings", type=("build", "run"))
    depends_on("r-structstrings", type=("build", "run"))
    depends_on("r-trna", type=("build", "run"))
    depends_on("r-biostrings", type=("build", "run"))
    depends_on("r-stringr", type=("build", "run"))
    depends_on("r-httr2", type=("build", "run"))
    depends_on("r-xml2", type=("build", "run"))
    depends_on("r-s4vectors", type=("build", "run"))
    depends_on("r-iranges", type=("build", "run"))
