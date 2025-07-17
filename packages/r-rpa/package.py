# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRpa(RPackage):
    """RPA: Robust Probabilistic Averaging for probe-level analysis

    Probabilistic analysis of probe reliability and differential gene expression on short oligonucleotide arrays.
    """

    homepage = "https://github.com/antagomir/RPA"
    bioc = "RPA"

    version("1.64.0", commit="7a8fc60f441f18fd44f3b8f2b3435f9fb64210a9")
    version("1.58.0", commit="8684bc98c30cecb8efb2bc02178a4e7d7e3378d1")

    depends_on("r@3.1.1:", type=("build", "run"))
    depends_on("r-affy", type=("build", "run"))
    depends_on("r-biocgenerics", type=("build", "run"))
    depends_on("r-biocstyle", type=("build", "run"))
    depends_on("r-rmarkdown", type=("build", "run"))
    depends_on("r-phyloseq", type=("build", "run"))
