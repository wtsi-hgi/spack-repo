# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRbiopaxparser(RPackage):
    """Parses BioPax files and represents them in R

    Parses BioPAX files and represents them in R, at the moment BioPAX level 2 and level 3 are supported.
    """

    homepage = "https://github.com/frankkramer-lab/rBiopaxParser"
    bioc = "rBiopaxParser"

    version("2.48.0", commit="af5ebe62eae4d30e1b4eb0bbbf8e249fb4741afe")
    version("2.42.0", commit="a4d31651ca1194afaea5a0191fa60489ef093af0")

    depends_on("r@4:", type=("build", "run"))
    depends_on("r-data-table", type=("build", "run"))
    depends_on("r-xml", type=("build", "run"))
