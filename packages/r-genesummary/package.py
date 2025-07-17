# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGenesummary(RPackage):
    """RefSeq Gene Summaries

    This package provides long description of genes collected from the RefSeq database. The text in "COMMENT" section started with "Summary" is extracted as the description of the gene. The long text descriptions can be used for analysis such as text mining.
    """

    homepage = "https://github.com/jokergoo/GeneSummary"
    bioc = "GeneSummary"

    version("0.99.6", commit="4ac4046ed6d9e91edff6361dfdae046c0ab7e9ed")
    version("0.99.6", commit="4ac4046ed6d9e91edff6361dfdae046c0ab7e9ed")

    depends_on("r@4:", type=("build", "run"))
