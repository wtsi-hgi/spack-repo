# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAsafe(RPackage):
    """Ancestry Specific Allele Frequency Estimation

    Given admixed individuals' bi-allelic SNP genotypes and ancestry pairs (where each ancestry can take one of three values) for multiple SNPs, perform an EM algorithm to deal with the fact that SNP genotypes are unphased with respect to ancestry pairs, in order to estimate ancestry-specific allele frequencies for all SNPs.
    """

    bioc = "ASAFE"

    version("1.34.0", commit="82f37decb3fa3da78dc45cc4b1d56f92ff6b16d0")
    version("1.28.0", commit="6436f199f6e398a61be6c34258b15e5da4d7973b")

    depends_on("r@3.2:", type=("build", "run"))
