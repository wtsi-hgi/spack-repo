# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBsseqdata(RPackage):
    """Example whole genome bisulfite data for the bsseq package

    Example whole genome bisulfite data for the bsseq package
    """

    bioc = "bsseqData"

    version("0.46.0", commit="f4f66f08544718854d0bcf825af6b0c52d5c3b53")
    version("0.40.0", commit="d52a6d22d58a0335cc03aa41e70cc853b0657e9f")

    depends_on("r@3.5:", type=("build", "run"))
    depends_on("r-bsseq@1.16:", type=("build", "run"))
