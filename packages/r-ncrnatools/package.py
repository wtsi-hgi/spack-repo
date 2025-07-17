# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNcrnatools(RPackage):
    """An R toolkit for non-coding RNA

    ncRNAtools provides a set of basic tools for handling and analyzing non-coding RNAs. These include tools to access the RNAcentral database and to predict and visualize the secondary structure of non-coding RNAs. The package also provides tools to read, write and interconvert the file formats most commonly used for representing such secondary structures.
    """

    bioc = "ncRNAtools"

    version("1.18.0", commit="ecd9ba66cd71ce74bbab4bd3fedc9121148e937a")
    version("1.12.0", commit="95cfa949efce81a7508d997468df24098be0a3da")

    depends_on("r-httr", type=("build", "run"))
    depends_on("r-xml2", type=("build", "run"))
    depends_on("r-ggplot2", type=("build", "run"))
    depends_on("r-iranges", type=("build", "run"))
    depends_on("r-genomicranges", type=("build", "run"))
    depends_on("r-s4vectors", type=("build", "run"))
