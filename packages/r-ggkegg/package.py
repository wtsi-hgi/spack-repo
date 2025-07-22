# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGgkegg(RPackage):
    """KEGG pathway visualization by ggplot2

    This package aims to import, parse, and analyze KEGG data such as KEGG PATHWAY and KEGG MODULE. The package supports visualizing KEGG information using ggplot2 and ggraph through using the grammar of graphics. The package enables the direct visualization of the results from various omics analysis packages.
    """

    homepage = "https://github.com/noriakis/ggkegg"
    bioc = "ggkegg"

    version("1.6.0", commit="369ed875c5c320a19c02f7c115647b409ea30d62")
    version("1.0.13", commit="8d6e75930cb3989fae04bbd42794636c87f7028d")

    depends_on("r@4.3:", type=("build", "run"))
    depends_on("r-ggplot2", type=("build", "run"))
    depends_on("r-ggraph", type=("build", "run"))
    depends_on("r-xml", type=("build", "run"))
    depends_on("r-igraph", type=("build", "run"))
    depends_on("r-tidygraph", type=("build", "run"))
    depends_on("r-biocfilecache", type=("build", "run"))
    depends_on("r-getoptlong", type=("build", "run"))
    depends_on("r-data-table", type=("build", "run"))
    depends_on("r-dplyr", type=("build", "run"))
    depends_on("r-magick", type=("build", "run"))
    depends_on("r-patchwork", type=("build", "run"))
    depends_on("r-shadowtext", type=("build", "run"))
    depends_on("r-stringr", type=("build", "run"))
    depends_on("r-tibble", type=("build", "run"))
    depends_on("r-org-hs-eg-db", type=("build", "run"))
    depends_on("r-annotationdbi", type=("build", "run"))
    depends_on("r-gtable", type=("build", "run"))
