# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RChromheatmap(RPackage):
    """Heat map plotting by genome coordinate

    The ChromHeatMap package can be used to plot genome-wide data (e.g. expression, CGH, SNP) along each strand of a given chromosome as a heat map. The generated heat map can be used to interactively identify probes and genes of interest.
    """

    bioc = "ChromHeatMap"

    version("1.62.0", commit="fdfff1bf9a14475fefb10998b502cbf26e52d732")
    version("1.56.0", commit="453e6887c78235a8aadda63d50fbf972fda8916a")

    depends_on("r@2.9:", type=("build", "run"))
    depends_on("r-biocgenerics@0.3.2:", type=("build", "run"))
    depends_on("r-annotate@1.20:", type=("build", "run"))
    depends_on("r-annotationdbi@1.4:", type=("build", "run"))
    depends_on("r-biobase@2.17.8:", type=("build", "run"))
    depends_on("r-iranges", type=("build", "run"))
    depends_on("r-rtracklayer", type=("build", "run"))
    depends_on("r-genomicranges", type=("build", "run"))
