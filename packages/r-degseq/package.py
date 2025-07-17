# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDegseq(RPackage):
    """Identify Differentially Expressed Genes from RNA-seq data

    DEGseq is an R package to identify differentially expressed genes from RNA-Seq data.
    """

    bioc = "DEGseq"

    version("1.62.0", commit="bed49dfa46d2445da534b4be39b4391f5d8b4527")
    version("1.56.1", commit="efe72265801b683e5b8605b5f2b823446f2ee670")

    depends_on("r@2.8:", type=("build", "run"))
    depends_on("r-qvalue", type=("build", "run"))
