# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REximir(RPackage):
    """R functions for the normalization of Exiqon miRNA array data

    This package contains functions for reading raw data in ImaGene TXT format obtained from Exiqon miRCURY LNA arrays, annotating them with appropriate GAL files, and normalizing them using a spike-in probe-based method. Other platforms and data formats are also supported.
    """

    bioc = "ExiMiR"

    version("2.50.0", commit="08eba458eb9328b7692462d170efd93843e91c8f")
    version("2.44.0", commit="45c5a7fabda25772323cc8c549ed559707e8161c")

    depends_on("r@2.10:", type=("build", "run"))
    depends_on("r-biobase@2.5.5:", type=("build", "run"))
    depends_on("r-affy@1.26.1:", type=("build", "run"))
    depends_on("r-limma", type=("build", "run"))
    depends_on("r-affyio@1.13.3:", type=("build", "run"))
    depends_on("r-preprocesscore@1.10:", type=("build", "run"))
