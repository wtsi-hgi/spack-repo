# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPwmenrich(RPackage):
    """PWM enrichment analysis

    A toolkit of high-level functions for DNA motif scanning and enrichment analysis built upon Biostrings. The main functionality is PWM enrichment analysis of already known PWMs (e.g. from databases such as MotifDb), but the package also implements high-level functions for PWM scanning and visualisation. The package does not perform "de novo" motif discovery, but is instead focused on using motifs that are either experimentally derived or computationally constructed by other tools.
    """

    bioc = "PWMEnrich"

    version("4.44.0", commit="9eb39703a7559e8061d8f8a62177187778dee098")
    version("4.38.0", commit="5c2bd63df7d00930f6e1c587e879af0b6ffa31e7")

    depends_on("r@3.5:", type=("build", "run"))
    depends_on("r-biocgenerics", type=("build", "run"))
    depends_on("r-biostrings", type=("build", "run"))
    depends_on("r-seqlogo", type=("build", "run"))
    depends_on("r-gdata", type=("build", "run"))
    depends_on("r-evd", type=("build", "run"))
    depends_on("r-s4vectors", type=("build", "run"))
