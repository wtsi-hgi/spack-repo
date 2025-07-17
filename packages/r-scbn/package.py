# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RScbn(RPackage):
    """A statistical normalization method and differential expression analysis for RNA-seq data between different species

    This package provides a scale based normalization (SCBN) method to identify genes with differential expression between different species. It takes into account the available knowledge of conserved orthologous genes and the hypothesis testing framework to detect differentially expressed orthologous genes. The method on this package are described in the article 'A statistical normalization method and differential expression analysis for RNA-seq data between different species' by Yan Zhou, Jiadi Zhu, Tiejun Tong, Junhui Wang, Bingqing Lin, Jun Zhang (2018, pending publication).
    """

    bioc = "SCBN"

    version("1.26.0", commit="c52accdae63665cc509d4f6158c819cb639e7116")
    version("1.20.0", commit="59e3bf85091d712aed4f03a22f1eaa54bde94dc8")

    depends_on("r@3.5:", type=("build", "run"))
