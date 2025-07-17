# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RUniprotWs(RPackage):
    """R Interface to UniProt Web Services

    The Universal Protein Resource (UniProt) is a comprehensive resource for protein sequence and annotation data. This package provides a collection of functions for retrieving, processing, and re-packaging UniProt web services. The package makes use of UniProt's modernized REST API and allows mapping of identifiers accross different databases.
    """

    homepage = "https://github.com/Bioconductor/UniProt.ws"
    bioc = "UniProt.ws"

    version("2.48.0", commit="d0e016bd675d4667f311e1d0fc7ac5c9b0963742")
    version("2.42.0", commit="72fb35bf5226adce5e2867fda7be01323f6f959c")

    depends_on("r-biocgenerics", type=("build", "run"))
    depends_on("r-rsqlite", type=("build", "run"))
    depends_on("r-annotationdbi", type=("build", "run"))
    depends_on("r-biocfilecache", type=("build", "run"))
    depends_on("r-biocbaseutils", type=("build", "run"))
    depends_on("r-httr", type=("build", "run"))
    depends_on("r-httpcache", type=("build", "run"))
    depends_on("r-jsonlite", type=("build", "run"))
    depends_on("r-progress", type=("build", "run"))
    depends_on("r-rjsoncons", type=("build", "run"))
