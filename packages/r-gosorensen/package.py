# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGosorensen(RPackage):
    """Statistical inference based on the Sorensen-Dice dissimilarity and the Gene Ontology (GO)

    This package implements inferential methods to compare gene lists in terms of their biological meaning as expressed in the GO. The compared gene lists are characterized by cross-tabulation frequency tables of enriched GO items. Dissimilarity between gene lists is evaluated using the Sorensen-Dice index. The fundamental guiding principle is that two gene lists are taken as similar if they share a great proportion of common enriched GO items.
    """

    bioc = "goSorensen"

    version("1.10.0", commit="b1b685df623b0e288873e7eff1fd27728403c040")
    version("1.4.0", commit="397b1486355ea87f583331074118959b37e80f86")

    depends_on("r@4.3:", type=("build", "run"))
    depends_on("r-go-db", type=("build", "run"))
    depends_on("r-org-hs-eg-db", type=("build", "run"))
    depends_on("r-goprofiles", type=("build", "run"))
    depends_on("r-clusterprofiler", type=("build", "run"))
    depends_on("r-stringr", type=("build", "run"))
    depends_on("r@4.4:", when="@1.10.0:", type=("build", "run"))
