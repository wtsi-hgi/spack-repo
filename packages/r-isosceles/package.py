# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIsosceles(RPackage):
    """Isosceles (Isoforms from Single-Cell; Long-read Expression Suite) is an R
    package dedicated to transcript detection and quantification from long reads,
    supporting both bulk RNA-Seq and scRNA-Seq technologies."""

    homepage = "https://github.com/Genentech/Isosceles"
    url = "https://github.com/Genentech/Isosceles/archive/refs/tags/0.2.1.tar.gz"

    version("0.2.1", sha256="9809144d0fd3affc6471b8e13fa4a94ad1f921d4307d33cfac1f6554e2d93166")

    depends_on("r@4.1:", type=("build", "run"))
    depends_on("r-biocmanager", type=("build", "run"))
    depends_on("r-scran", type=("build", "run"))
    depends_on("r-scater", type=("build", "run"))
    depends_on("r-uwot", type=("build", "run"))
    depends_on("r-dittoseq", type=("build", "run"))
    depends_on("r-dexseq", type=("build", "run"))
    depends_on("r-nebulosa", type=("build", "run"))
    depends_on("r-ggbio", type=("build", "run"))
    depends_on("r-biocstyle", type=("build", "run"))
    depends_on("r-assertthat", type=("build", "run"))
    depends_on("r-fastmatch", type=("build", "run"))
