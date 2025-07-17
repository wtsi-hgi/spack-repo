# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpikeli(RPackage):
    """Affymetrix Spike-in Langmuir Isotherm Data Analysis Tool

    SpikeLI is a package that performs the analysis of the Affymetrix spike-in data using the Langmuir Isotherm. The aim of this package is to show the advantages of a physical-chemistry based analysis of the Affymetrix microarray data compared to the traditional methods. The spike-in (or Latin square) data for the HGU95 and HGU133 chipsets have been downloaded from the Affymetrix web site. The model used in the spikeLI package is described in details in E. Carlon and T. Heim, Physica A 362, 433 (2006).
    """

    bioc = "spikeLI"

    version("2.68.0", commit="87d027ed256f88ebca387a7bdb87c93f7cb2ab6e")
    version("2.62.0", commit="95a6445c0d67af0221ea4e8da4f97545784a8744")
