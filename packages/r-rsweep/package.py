# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRsweep(RPackage):
    """Functions to creation of low dimensional comparative matrices of Amino Acid Sequence occurrences

    The SWeeP method was developed to favor the analizes between amino acids sequences and to assist alignment free phylogenetic studies. This method is based on the concept of sparse words, which is applied in the scan of biological sequences and its the conversion in a matrix of ocurrences. Aiming the generation of low dimensional matrices of Amino Acid Sequence occurrences.
    """

    bioc = "rSWeeP"

    version("1.20.0", commit="6c643705675088cf983fd4d299364fc8f4b043e7")
    version("1.14.0", commit="606d584fbd8157680c42fab96aaa37d36962049d")

    depends_on("r@4:", type=("build", "run"))
    depends_on("r-pracma", type=("build", "run"))
