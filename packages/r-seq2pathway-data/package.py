# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSeq2pathwayData(RPackage):
    """data set for R package seq2pathway

    Supporting data for the seq2patheway package. Includes modified gene sets from MsigDB and org.Hs.eg.db; gene locus definitions from GENCODE project.
    """

    bioc = "seq2pathway.data"

    version("1.40.0", commit="b0a8b5392a2f2830f141cf5e9c1c70ade6953bc7")
    version("1.34.0", commit="ba45f9b30de51fa88c22ac7cf2ac5b8d37ce53df")

    depends_on("r@3.6.2:", type=("build", "run"))
