# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDyebias(RPackage):
    """The GASSCO method for correcting for slide-dependent gene-specific dye bias

    Many two-colour hybridizations suffer from a dye bias that is both gene-specific and slide-specific. The former depends on the content of the nucleotide used for labeling; the latter depends on the labeling percentage. The slide-dependency was hitherto not recognized, and made addressing the artefact impossible.  Given a reasonable number of dye-swapped pairs of hybridizations, or of same vs. same hybridizations, both the gene- and slide-biases can be estimated and corrected using the GASSCO method (Margaritis et al., Mol. Sys. Biol. 5:266 (2009), doi:10.1038/msb.2009.21)
    """

    homepage = "http://www.holstegelab.nl/publications/margaritis_lijnzaad"
    bioc = "dyebias"

    version("1.68.0", commit="72dd03486397f333f3b079e6f5dde9637bec7b17")
    version("1.62.0", commit="37a71001256808543cc031984ef11ba797dd80ff")

    depends_on("r@1.4.1:", type=("build", "run"))
    depends_on("r-marray", type=("build", "run"))
    depends_on("r-biobase", type=("build", "run"))
