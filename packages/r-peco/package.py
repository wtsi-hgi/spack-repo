# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPeco(RPackage):
    """A Supervised Approach for **P**r**e**dicting **c**ell Cycle Pr**o**gression using scRNA-seq data

    Our approach provides a way to assign continuous cell cycle phase using scRNA-seq data, and consequently, allows to identify cyclic trend of gene expression levels along the cell cycle. This package provides method and training data, which includes scRNA-seq data collected from 6 individual cell lines of induced pluripotent stem cells (iPSCs), and also continuous cell cycle phase derived from FUCCI fluorescence imaging data.
    """

    homepage = "https://github.com/jhsiao999/peco"
    bioc = "peco"

    version("1.20.0", commit="a577f45417ce9c647a4ab851310378477a046556")
    version("1.14.0", commit="52a5c2d0ce022c81ae84adc51080b517651dc0fe")

    depends_on("r@3.5:", type=("build", "run"))
    depends_on("r-assertthat", type=("build", "run"))
    depends_on("r-circular", type=("build", "run"))
    depends_on("r-conicfit", type=("build", "run"))
    depends_on("r-doparallel", type=("build", "run"))
    depends_on("r-foreach", type=("build", "run"))
    depends_on("r-genlasso@1.4:", type=("build", "run"))
    depends_on("r-scater", type=("build", "run"))
    depends_on("r-singlecellexperiment", type=("build", "run"))
    depends_on("r-summarizedexperiment", type=("build", "run"))
