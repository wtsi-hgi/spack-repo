# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSystempiperdata(RPackage):
    """systemPipeRdata: Workflow templates and sample data

    systemPipeRdata is a helper package to generate with a single command NGS workflow templates that are intended to be used by its parent package systemPipeR. The latter is an environment for building end-to-end analysis pipelines with automated report generation for next generation sequence (NGS) applications such as RNA-Seq, RIBO-Seq, ChIP-Seq, VAR-Seq and many others. Detailed examples for using systemPipeRdata are given in systemPipeR's overview vignette.
    """

    homepage = "https://github.com/tgirke/systemPipeRdata"
    bioc = "systemPipeRdata"

    version("2.12.2", commit="9ad596e0bce84257a43cb66dc8d66f6286fa7f62")
    version("2.6.0", commit="b3365d5421e5d83d521b4172f6af2655f7d7a95a")

    depends_on("r-biostrings", type=("build", "run"))
    depends_on("r-biocgenerics", type=("build", "run"))
    depends_on("r-jsonlite", type=("build", "run"))
    depends_on("r-remotes", type=("build", "run"))
