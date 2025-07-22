# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRmspc(RPackage):
    """Multiple Sample Peak Calling

    The rmspc package runs MSPC (Multiple Sample Peak Calling) software using R. The analysis of ChIP-seq samples outputs a number of enriched regions (commonly known as "peaks"), each indicating a protein-DNA interaction or a specific chromatin modification. When replicate samples are analyzed, overlapping peaks are expected. This repeated evidence can therefore be used to locally lower the minimum significance required to accept a peak. MSPC uses combined evidence from replicated experiments to evaluate peak calling output, rescuing peaks, and reduce false positives. It takes any number of replicates as input and improves sensitivity and specificity of peak calling on each, and identifies consensus regions between the input samples.
    """

    homepage = "https://genometric.github.io/MSPC/"
    bioc = "rmspc"

    version("1.14.0", commit="7ecf48e2a05843f8b3ec8a23d7fe5268f32dd0e7")
    version("1.8.0", commit="4214dd6f31c70055887834222692f481dd1fd5dc")

    depends_on("r-processx", type=("build", "run"))
    depends_on("r-biocmanager", type=("build", "run"))
    depends_on("r-rtracklayer", type=("build", "run"))
    depends_on("r-genomicranges", type=("build", "run"))
    depends_on("r-stringr", type=("build", "run"))
    depends_on("mono@6:", type=("build", "link", "run"))
