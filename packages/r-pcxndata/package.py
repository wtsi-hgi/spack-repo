# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPcxndata(RPackage):
    """Correlation coefficients and p values between pre-defined pathway/gene sets

    PCxN database contains correlation coefficients and p values between pre-defined gene sets within MSigDB H hallmark gene sets, MSigDB C2 CP (Canonical pathways), MSigDB C5 GO BP gene sets and Pathprint respectively, as well as adjusted pathway correlations to account for the shared genes between pathway pairs.
    """

    bioc = "pcxnData"

    version("2.24.0", commit="a61d0af46aab4b07f6b2f0d819ed5553f8b3443e")

    depends_on("r@3.4:", type=("build", "run"))
