# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRgenometracks(RPackage):
    """Integerated visualization of epigenomic data

    rGenomeTracks package leverages the power of pyGenomeTracks software with the interactivity of R. pyGenomeTracks is a python software that offers robust method for visualizing epigenetic data files like narrowPeak, Hic matrix, TADs and arcs, however though, here is no way currently to use it within R interactive session. rGenomeTracks wrapped the whole functionality of pyGenomeTracks with additional utilites to make to more pleasant for R users.
    """

    bioc = "rGenomeTracks"

    version("1.14.0", commit="3502b4c3c4d74a7966d8e2c59962d5c707ec04c5")
    version("1.8.0", commit="3bc3e070aa5c3913e775e41e5b4007c768eccd92")

    depends_on("r@4.1:", type=("build", "run"))
    depends_on("r-imager", type=("build", "run"))
    depends_on("r-reticulate", type=("build", "run"))
    depends_on("r-rgenometracksdata", type=("build", "run"))
