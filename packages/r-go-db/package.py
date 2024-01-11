# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class RGoDb(RPackage):
    """A set of annotation maps describing the entire Gene Ontology assembled using data from GO."""

    url = "https://bioconductor.org/packages/release/data/annotation/src/contrib/GO.db_3.18.0.tar.gz"
    bioc = "GO.db"

    version("3.18.0", sha256="f580341e7fd19efa3e5789b993dd8ef0cf813a45c49a647a173c6f49c451d87e")

    depends_on("r-annotationdbi", type=("build", "run"))
