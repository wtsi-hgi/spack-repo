# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REatonetalchipseq(RPackage):
    """ChIP-seq data of ORC-binding sites in Yeast excerpted from Eaton et al. 2010

    ChIP-seq analysis subset from "Conserved nucleosome positioning defines replication origins" (PMID 20351051)
    """

    bioc = "EatonEtAlChIPseq"

    version("0.46.0", commit="01a07b961581a730e55322f4407d804c7f41fc8b")
    version("0.40.0", commit="9750f419ef3efca6812644ef6ac5e759fda28b14")

    depends_on("r-genomicranges@1.5.42:", type=("build", "run"))
    depends_on("r-shortread", type=("build", "run"))
    depends_on("r-rtracklayer", type=("build", "run"))
