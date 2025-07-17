# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBlma(RPackage):
    """BLMA: A package for bi-level meta-analysis

    Suit of tools for bi-level meta-analysis. The package can be used in a wide range of applications, including general hypothesis testings, differential expression analysis, functional analysis, and pathway analysis.
    """

    bioc = "BLMA"

    version("1.32.0", commit="37134c51fc30c9a1133ef00d2cb6c5a635ead535")
    version("1.26.0", commit="c63d0ef5dba53bbe5639ab60a96916045b71a42b")

    depends_on("r-rontotools", type=("build", "run"))
    depends_on("r-gsa", type=("build", "run"))
    depends_on("r-padog", type=("build", "run"))
    depends_on("r-limma", type=("build", "run"))
    depends_on("r-graph", type=("build", "run"))
    depends_on("r-biobase", type=("build", "run"))
    depends_on("r-metafor", type=("build", "run"))
