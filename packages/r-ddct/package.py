# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDdct(RPackage):
    """The ddCt Algorithm for the Analysis of Quantitative Real-Time PCR (qRT-PCR)

    The Delta-Delta-Ct (ddCt) Algorithm is an approximation method to determine relative gene expression with quantitative real-time PCR (qRT-PCR) experiments. Compared to other approaches, it requires no standard curve for each primer-target pair, therefore reducing the working load and yet returning accurate enough results as long as the assumptions of the amplification efficiency hold. The ddCt package implements a pipeline to collect, analyse and visualize qRT-PCR results, for example those from TaqMan SDM software, mainly using the ddCt method. The pipeline can be either invoked by a script in command-line or through the API consisting of S4-Classes, methods and functions.
    """

    bioc = "ddCt"

    version("1.64.0", commit="ed9b832e462ade62712d1a55105fd186e8d8b81f")
    version("1.58.0", commit="33ff3d4decbb3c9da41ff497b35d8130bed192b2")

    depends_on("r@2.3:", type=("build", "run"))
    depends_on("r-biobase@1.10:", type=("build", "run"))
    depends_on("r-rcolorbrewer@0.1.3:", type=("build", "run"))
    depends_on("r-xtable", type=("build", "run"))
    depends_on("r-lattice", type=("build", "run"))
    depends_on("r-biocgenerics", type=("build", "run"))
