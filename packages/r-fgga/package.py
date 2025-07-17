# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFgga(RPackage):
    """Hierarchical ensemble method based on factor graph

    Package that implements the FGGA algorithm. This package provides a hierarchical ensemble method based ob factor graphs for the consistent cross-ontology annotation of protein coding genes. FGGA embodies elements of predicate logic, communication theory, supervised learning and inference in graphical models.
    """

    homepage = "https://github.com/fspetale/fgga"
    bioc = "fgga"

    version("1.16.0", commit="74a4c71895f4af43a019ca0c54cd627cd60b4add")
    version("1.10.2", commit="999b166863570ab4d681a42ea178d26f6510f057")

    depends_on("r@4.3:", type=("build", "run"))
    depends_on("r-rbgl", type=("build", "run"))
    depends_on("r-graph", type=("build", "run"))
    depends_on("r-e1071", type=("build", "run"))
    depends_on("r-grbase", type=("build", "run"))
    depends_on("r-jsonlite", type=("build", "run"))
    depends_on("r-biocfilecache", type=("build", "run"))
    depends_on("r-curl", type=("build", "run"))
    depends_on("r-igraph", type=("build", "run"))
