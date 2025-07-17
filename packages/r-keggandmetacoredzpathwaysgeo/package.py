# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKeggandmetacoredzpathwaysgeo(RPackage):
    """Disease Datasets from GEO

    This is a collection of 18 data sets for which the phenotype is a disease with a corresponding pathway in either KEGG or metacore database.This collection of datasets were used as gold standard in comparing gene set analysis methods.
    """

    bioc = "KEGGandMetacoreDzPathwaysGEO"

    version("1.28.0", commit="fb4d093a4fa8f66c15f0f104da6cc8d8a0f3f756")
    version("1.22.0", commit="450757a05ca18992b2bd7bb3a0625a5841d3fdb7")

    depends_on("r@2.15:", type=("build", "run"))
    depends_on("r-biobase", type=("build", "run"))
    depends_on("r-biocgenerics", type=("build", "run"))
