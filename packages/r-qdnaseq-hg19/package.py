# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQdnaseqHg19(RPackage):
    """QDNAseq bin annotation for hg19

    This package provides QDNAseq bin annotations for the human genome build hg19.
    """

    homepage = "https://github.com/tgac-vumc/QDNAseq.hg19"
    bioc = "QDNAseq.hg19"

    version("1.38.0", commit="f1e95f00afdc53b7c37c07a075ad8c2a4e734355")
    version("1.32.0", commit="6a5bd78e9b68103c2c81f12f7bb9fd7bb388c3df")

    depends_on("r@3.2.1:", type=("build", "run"))
    depends_on("r-qdnaseq", type=("build", "run"))
