# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMacorrplot(RPackage):
    """Visualize artificial correlation in microarray data

    Graphically displays correlation in microarray data that is due to insufficient normalization
    """

    homepage = (
        "http://www.pubmedcentral.gov/articlerender.fcgi?tool=pubmed&pubmedid=15799785"
    )
    bioc = "maCorrPlot"

    version("1.78.0", commit="4a710eb320eb48a96907f963f645caaa796fbadc")
    version("1.72.0", commit="84bc62191c6b1e901d1df8c548600738296a9e60")

    depends_on("r-lattice", type=("build", "run"))
