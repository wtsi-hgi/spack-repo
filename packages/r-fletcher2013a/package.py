# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFletcher2013a(RPackage):
    """Gene expression data from breast cancer cells under FGFR2 signalling perturbation

    The package Fletcher2013a contains time-course gene expression data from MCF-7 cells treated under different experimental systems in order to perturb FGFR2 signalling. The data comes from Fletcher et al. (Nature Comms 4:2464, 2013) where further details about the background and the experimental design of the study can be found.
    """

    homepage = "http://dx.doi.org/10.1038/ncomms3464"
    bioc = "Fletcher2013a"

    version("1.44.0", commit="b4c9950cd4594c323f945f07e508aeb47a5b9a3d")
    version("1.38.0", commit="8b745f266655c85a817462a2b5370de270635bb2")

    depends_on("r@2.15:", type=("build", "run"))
    depends_on("r-limma", type=("build", "run"))
    depends_on("r-biobase", type=("build", "run"))
    depends_on("r-venndiagram", type=("build", "run"))
    depends_on("r-gplots", type=("build", "run"))
