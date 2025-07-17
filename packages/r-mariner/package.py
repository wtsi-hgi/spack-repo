# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMariner(RPackage):
    """Mariner: Explore the Hi-Cs

    Tools for manipulating paired ranges and working with Hi-C data in R. Functionality includes manipulating/merging paired regions, generating paired ranges, extracting/aggregating interactions from `.hic` files, and visualizing the results. Designed for compatibility with plotgardener for visualization.
    """

    homepage = "http://ericscottdavis.com/mariner/"
    bioc = "mariner"

    version("1.8.1", commit="192d48a7ab80b939ecc233aabe54be064e0a5ee8")
    version("1.2.0", commit="9906b3239fefe8a51e3343b648cbc2dfcdfeb806")

    depends_on("r@4.2:", type=("build", "run"))
    depends_on("r-s4vectors", type=("build", "run"))
    depends_on("r-biocgenerics", type=("build", "run"))
    depends_on("r-biocmanager", type=("build", "run"))
    depends_on("r-genomicranges", type=("build", "run"))
    depends_on("r-interactionset", type=("build", "run"))
    depends_on("r-data-table", type=("build", "run"))
    depends_on("r-rlang", type=("build", "run"))
    depends_on("r-glue", type=("build", "run"))
    depends_on("r-assertthat", type=("build", "run"))
    depends_on("r-plyranges", type=("build", "run"))
    depends_on("r-magrittr", type=("build", "run"))
    depends_on("r-dbscan", type=("build", "run"))
    depends_on("r-purrr", type=("build", "run"))
    depends_on("r-progress", type=("build", "run"))
    depends_on("r-genomeinfodb", type=("build", "run"))
    depends_on("r-strawr@0.0.91:", type=("build", "run"))
    depends_on("r-delayedarray", type=("build", "run"))
    depends_on("r-hdf5array", type=("build", "run"))
    depends_on("r-abind", type=("build", "run"))
    depends_on("r-biocparallel", type=("build", "run"))
    depends_on("r-iranges", type=("build", "run"))
    depends_on("r-summarizedexperiment", type=("build", "run"))
    depends_on("r-rhdf5", type=("build", "run"))
    depends_on("r-plotgardener", type=("build", "run"))
    depends_on("r-rcolorbrewer", type=("build", "run"))
    depends_on("r-colourvalues", type=("build", "run"))
