# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RScreenr(RPackage):
    """Package to Perform High Throughput Biological Screening

    ScreenR is a package suitable to perform hit identification in loss of function High Throughput Biological Screenings performed using barcoded shRNA-based libraries. ScreenR combines the computing power of software such as edgeR with the simplicity of use of the Tidyverse metapackage. ScreenR executes a pipeline able to find candidate hits from barcode counts, and integrates a wide range of visualization modes for each step of the analysis.
    """

    homepage = "https://emanuelsoda.github.io/ScreenR/"
    bioc = "ScreenR"

    version("1.10.0", commit="4b7b6cccc2f62ad567f9ac51163d1e8594021f50")
    version("1.4.0", commit="36bfecba0686233ca2596e6901680cac629edc7d")

    depends_on("r@4.2:", type=("build", "run"))
    depends_on("r-rlang@0.4:", type=("build", "run"))
    depends_on("r-stringr@1.4:", type=("build", "run"))
    depends_on("r-limma@3.46:", type=("build", "run"))
    depends_on("r-patchwork@1.1:", type=("build", "run"))
    depends_on("r-tibble@3.1.6:", type=("build", "run"))
    depends_on("r-scales@1.1.1:", type=("build", "run"))
    depends_on("r-ggvenn@0.1.9:", type=("build", "run"))
    depends_on("r-purrr@0.3.4:", type=("build", "run"))
    depends_on("r-ggplot2@3.3:", type=("build", "run"))
    depends_on("r-tidyr@1.2:", type=("build", "run"))
    depends_on("r-magrittr@1:", type=("build", "run"))
    depends_on("r-dplyr@1:", type=("build", "run"))
    depends_on("r-edger@3.32:", type=("build", "run"))
    depends_on("r-tidyselect@1.1.2:", type=("build", "run"))
