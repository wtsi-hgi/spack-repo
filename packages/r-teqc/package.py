# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTeqc(RPackage):
    """Quality control for target capture experiments

    Target capture experiments combine hybridization-based (in solution or on microarrays) capture and enrichment of genomic regions of interest (e.g. the exome) with high throughput sequencing of the captured DNA fragments. This package provides functionalities for assessing and visualizing the quality of the target enrichment process, like specificity and sensitivity of the capture, per-target read coverage and so on.
    """

    bioc = "TEQC"

    version("4.30.0", commit="e59e99e67361f625c7a8ff80850a9cbb4deda3ef")
    version("4.24.0", commit="b13930a015e79833272298eee3af638ab4cf3202")

    depends_on("r-biocgenerics@0.1:", type=("build", "run"))
    depends_on("r-iranges@1.13.5:", type=("build", "run"))
    depends_on("r-rsamtools", type=("build", "run"))
    depends_on("r-hwriter", type=("build", "run"))
    depends_on("r-biobase@2.15.1:", type=("build", "run"))
