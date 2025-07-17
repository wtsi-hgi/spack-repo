# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBnbc(RPackage):
    """Bandwise normalization and batch correction of Hi-C data

    Tools to normalize (several) Hi-C data from replicates.
    """

    homepage = "https://github.com/hansenlab/bnbc"
    bioc = "bnbc"

    version("1.30.0", commit="f992cfe9f8f570361dc9d580f6b761dd7f07c370")
    version("1.24.2", commit="c80ab47a13fa20977ee2803eb6ba129f3f12525e")

    depends_on("r@3.5:", type=("build", "run"))
    depends_on("r-biocgenerics", type=("build", "run"))
    depends_on("r-summarizedexperiment", type=("build", "run"))
    depends_on("r-genomicranges", type=("build", "run"))
    depends_on("r-rcpp", type=("build", "run"))
    depends_on("r-iranges", type=("build", "run"))
    depends_on("r-rhdf5", type=("build", "run"))
    depends_on("r-data-table", type=("build", "run"))
    depends_on("r-genomeinfodb", type=("build", "run"))
    depends_on("r-s4vectors", type=("build", "run"))
    depends_on("r-matrixstats", type=("build", "run"))
    depends_on("r-preprocesscore", type=("build", "run"))
    depends_on("r-sva", type=("build", "run"))
    depends_on("r-ebimage", type=("build", "run"))
    depends_on("r-hicbricks", type=("build", "run"))
