# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPanp(RPackage):
    """Presence-Absence Calls from Negative Strand Matching Probesets

    A function to make gene presence/absence calls based on distance from negative strand matching probesets (NSMP) which are derived from Affymetrix annotation. PANP is applied after gene expression values are created, and therefore can be used after any preprocessing method such as MAS5 or GCRMA, or PM-only methods like RMA. NSMP sets have been established for the HGU133A and HGU133-Plus-2.0 chipsets to date.
    """

    bioc = "panp"

    version("1.78.0", commit="cb32fa4beb9a676a78240a6a968578e1fa85b886")
    version("1.72.0", commit="c6bcd889be1cc05d58a4e6c4e3f85a57d223657f")

    depends_on("r@2.10:", type=("build", "run"))
    depends_on("r-affy@1.23.4:", type=("build", "run"))
    depends_on("r-biobase", type=("build", "run"))
