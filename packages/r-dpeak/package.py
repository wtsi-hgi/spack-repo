# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDpeak(RPackage):
    """dPeak (Deconvolution of Peaks in ChIP-seq Analysis)

    dPeak is a statistical framework for the high resolution identification of protein-DNA interaction sites using PET and SET ChIP-Seq and ChIP-exo data. It provides computationally efficient and user friendly interface to process ChIP-seq and ChIP-exo data, implement exploratory analysis, fit dPeak model, and export list of predicted binding sites for downstream analysis.
    """

    bioc = "dpeak"

    version("1.14.0", commit="174adc9519bfb78fc899ab91e020991df80dc2ce")

    depends_on("r@4:", type=("build", "run"))
    depends_on("r-rcpp", type=("build", "run"))
    depends_on("r-mass", type=("build", "run"))
    depends_on("r-iranges", type=("build", "run"))
    depends_on("r-bsgenome", type=("build", "run"))
    depends_on("meme", type=("build", "link", "run"))
