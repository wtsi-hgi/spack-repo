# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSeqcat(RPackage):
    """High Throughput Sequencing Cell Authentication Toolkit

    The seqCAT package uses variant calling data (in the form of VCF files) from high throughput sequencing technologies to authenticate and validate the source, function and characteristics of biological samples used in scientific endeavours.
    """

    bioc = "seqCAT"

    version("1.30.0", commit="5a3cc853a29d5746c7c472f9d49e34712bb71504")
    version("1.24.0", commit="2a592c3fbde66bd34ed9369d3e6730d3dc933f58")

    depends_on("r@3.6:", type=("build", "run"))
    depends_on("r-genomicranges@1.26.4:", type=("build", "run"))
    depends_on("r-variantannotation@1.20.3:", type=("build", "run"))
    depends_on("r-dplyr@0.5:", type=("build", "run"))
    depends_on("r-genomeinfodb@1.13.4:", type=("build", "run"))
    depends_on("r-ggplot2@2.2.1:", type=("build", "run"))
    depends_on("r-iranges@2.8.2:", type=("build", "run"))
    depends_on("r-rtracklayer", type=("build", "run"))
    depends_on("r-rlang", type=("build", "run"))
    depends_on("r-scales@0.4.1:", type=("build", "run"))
    depends_on("r-s4vectors@0.12.2:", type=("build", "run"))
    depends_on("r-summarizedexperiment@1.4:", type=("build", "run"))
    depends_on("r-tidyr@0.6.1:", type=("build", "run"))
