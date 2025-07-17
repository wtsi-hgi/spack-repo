# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRnamodrRibomethseq(RPackage):
    """Detection of 2'-O methylations by RiboMethSeq

    RNAmodR.RiboMethSeq implements the detection of 2'-O methylations on RNA from experimental data generated with the RiboMethSeq protocol. The package builds on the core functionality of the RNAmodR package to detect specific patterns of the modifications in high throughput sequencing data.
    """

    homepage = "https://github.com/FelixErnst/RNAmodR.RiboMethSeq"
    bioc = "RNAmodR.RiboMethSeq"

    version("1.22.0", commit="3a9e7fb8e093d735842ab5748fed481e353b2b78")
    version("1.16.0", commit="1dba6360eec6f3941f1f560ac55cad6dfd723601")

    depends_on("r@4:", type=("build", "run"))
    depends_on("r-rnamodr@1.5.3:", type=("build", "run"))
    depends_on("r-s4vectors", type=("build", "run"))
    depends_on("r-biocgenerics", type=("build", "run"))
    depends_on("r-iranges", type=("build", "run"))
    depends_on("r-genomicranges", type=("build", "run"))
    depends_on("r-gviz", type=("build", "run"))
