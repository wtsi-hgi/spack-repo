# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIdr2d(RPackage):
    """Irreproducible Discovery Rate for Genomic Interactions Data

    A tool to measure reproducibility between genomic experiments that produce two-dimensional peaks (interactions between peaks), such as ChIA-PET, HiChIP, and HiC. idr2d is an extension of the original idr package, which is intended for (one-dimensional) ChIP-seq peaks.
    """

    homepage = "https://idr2d.mit.edu"
    bioc = "idr2d"

    version("1.22.0", commit="fd9d6dd804d8f50bc4a9fa7b73d6f4f7ab651689")
    version("1.16.0", commit="4d9a966f5e6a95a183d48c4648342d6821b70a04")

    depends_on("r@3.6:", type=("build", "run"))
    depends_on("r-dplyr@0.7.6:", type=("build", "run"))
    depends_on("r-futile-logger@1.4.3:", type=("build", "run"))
    depends_on("r-genomeinfodb@1.14:", type=("build", "run"))
    depends_on("r-genomicranges@1.30:", type=("build", "run"))
    depends_on("r-ggplot2@3.1.1:", type=("build", "run"))
    depends_on("r-idr@1.2:", type=("build", "run"))
    depends_on("r-iranges@2.18:", type=("build", "run"))
    depends_on("r-magrittr@1.5:", type=("build", "run"))
    depends_on("r-reticulate@1.13:", type=("build", "run"))
    depends_on("r-scales@1:", type=("build", "run"))
    depends_on("r-stringr@1.3.1:", type=("build", "run"))
    depends_on("python@3.5.0:", type=("build", "link", "run"))
