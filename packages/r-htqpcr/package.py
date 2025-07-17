# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHtqpcr(RPackage):
    """Automated analysis of high-throughput qPCR data

    Analysis of Ct values from high throughput quantitative real-time PCR (qPCR) assays across multiple conditions or replicates. The input data can be from spatially-defined formats such ABI TaqMan Low Density Arrays or OpenArray; LightCycler from Roche Applied Science; the CFX plates from Bio-Rad Laboratories; conventional 96- or 384-well plates; or microfluidic devices such as the Dynamic Arrays from Fluidigm Corporation. HTqPCR handles data loading, quality assessment, normalization, visualization and parametric or non-parametric testing for statistical significance in Ct values between features (e.g. genes, microRNAs).
    """

    homepage = "http://www.ebi.ac.uk/bertone/software"
    bioc = "HTqPCR"

    version("1.62.0", commit="d2e6479663aea1a32c1b56e9f9cee1ba95d7006d")
    version("1.56.0", commit="cba77c7a16425bb6a0e239807af9bb817d00e492")

    depends_on("r-biobase", type=("build", "run"))
    depends_on("r-rcolorbrewer", type=("build", "run"))
    depends_on("r-limma", type=("build", "run"))
    depends_on("r-affy", type=("build", "run"))
    depends_on("r-gplots", type=("build", "run"))
