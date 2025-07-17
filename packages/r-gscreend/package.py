# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGscreend(RPackage):
    """Analysis of pooled genetic screens

    Package for the analysis of pooled genetic screens (e.g. CRISPR-KO). The analysis of such screens is based on the comparison of gRNA abundances before and after a cell proliferation phase. The gscreend packages takes gRNA counts as input and allows detection of genes whose knockout decreases or increases cell proliferation.
    """

    homepage = "https://github.com/imkeller/gscreend"
    bioc = "gscreend"

    version("1.22.0", commit="b325a7bf5a085bce9701d092c52a71db8acc8072")
    version("1.16.1", commit="c8d008c4512305a401ca26a8aaad60476056211f")
    version("1.16.0", commit="b3333031ccee5ec81e3c05a62d40cee335f100dc")

    depends_on("r@3.6:", type=("build", "run"))
    depends_on("r-summarizedexperiment", type=("build", "run"))
    depends_on("r-nloptr", type=("build", "run"))
    depends_on("r-fgarch", type=("build", "run"))
    depends_on("r-biocparallel", type=("build", "run"))
