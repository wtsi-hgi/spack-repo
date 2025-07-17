# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFmcsr(RPackage):
    """Mismatch Tolerant Maximum Common Substructure Searching

    The fmcsR package introduces an efficient maximum common substructure (MCS) algorithms combined with a novel matching strategy that allows for atom and/or bond mismatches in the substructures shared among two small molecules. The resulting flexible MCSs (FMCSs) are often larger than strict MCSs, resulting in the identification of more common features in their source structures, as well as a higher sensitivity in finding compounds with weak structural similarities. The fmcsR package provides several utilities to use the FMCS algorithm for pairwise compound comparisons, structure similarity searching and clustering.
    """

    homepage = "https://github.com/girke-lab/fmcsR"
    bioc = "fmcsR"

    version("1.50.0", commit="ee2ed1cb0a1f4640ed4b667b5ae448eee7002e5f")
    version("1.44.0", commit="08956ef324ebb1e5054f391521600938d8ead0e9")

    depends_on("r@2.10:", type=("build", "run"))
    depends_on("r-chemminer", type=("build", "run"))
    depends_on("r-runit", type=("build", "run"))
    depends_on("r-biocgenerics", type=("build", "run"))
