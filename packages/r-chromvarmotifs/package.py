# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RChromvarmotifs(RPackage):
    """Motifs for Use with chromVAR.

    Makes it easy to use several different motif collections in R, particularly
    for use with motifmatchr and chromVAR packages. Motifs are stored as
    PWMatrixList objects (object from TFBSTools package)."""

    homepage = "https://github.com/GreenleafLab/chromVARmotifs"
    url = "https://github.com/GreenleafLab/chromVARmotifs/archive/refs/tags/v1.0.0.tar.gz"
    git = "https://github.com/GreenleafLab/chromVARmotifs.git"

    version("20171117", commit="38bed559c1f4770b6c91c80bf3f8ea965da26076")

    depends_on("r@3.4.0:", type=("build", "run"))

    # Direct dependency mentioned in README
    depends_on("r-tfbstools", type=("build", "run"))
