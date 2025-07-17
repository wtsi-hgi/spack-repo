# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RScanmirdata(RPackage):
    """miRNA Affinity models for the scanMiR package

    This package contains companion data to the scanMiR package. It contains `KdModel` (miRNA 12-mer binding affinity models) collections corresponding to all human, mouse and rat mirbase miRNAs. See the scanMiR package for details.
    """

    bioc = "scanMiRData"

    version("1.14.0", commit="e9b652fb33d5e2a40c588671dd95ebafb0b52737")
    version("1.8.0", commit="112e8ff631cafecb02853aa600feeb9cb7f136c6")

    depends_on("r@4:", type=("build", "run"))
    depends_on("r-scanmir", type=("build", "run"))
