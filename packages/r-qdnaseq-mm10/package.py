# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQdnaseqMm10(RPackage):
    """Bin annotation mm10

    This package provides QDNAseq bin annotations for the mouse genome build mm10.
    """

    homepage = "https://github.com/tgac-vumc/QDNAseq.mm10"
    bioc = "QDNAseq.mm10"

    version("1.38.0", commit="8be83a6f81e50de79153242cc45ccb035b53a8e9")
    version("1.32.0", commit="91e71ca903c46d58b730e3282340c361da070484")

    depends_on("r@3.2.1:", type=("build", "run"))
    depends_on("r-qdnaseq", type=("build", "run"))
