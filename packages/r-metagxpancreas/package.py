# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMetagxpancreas(RPackage):
    """Transcriptomic Pancreatic Cancer Datasets

    A collection of pancreatic Cancer transcriptomic datasets that are part of the MetaGxData package compendium. This package contains multiple pancreas cancer datasets that have been downloaded from various resources and turned into SummarizedExperiment objects. The details of how the authors normalized the data can be found in the experiment data section of the objects. Additionally, the location the data was obtained from can be found in the url variables of the experiment data portion of each SE.
    """

    bioc = "MetaGxPancreas"

    version("1.28.0", commit="81a376590b5100f2bb84fefedaa902f677702baf")
    version("1.22.0", commit="1f86cdff79a1c98c456c89c5b66a5ed493fd7ab3")

    depends_on("r-summarizedexperiment", type=("build", "run"))
    depends_on("r-experimenthub", type=("build", "run"))
    depends_on("r@3.6:", type=("build", "run"))
    depends_on("r-impute", type=("build", "run"))
    depends_on("r-s4vectors", type=("build", "run"))
    depends_on("r-annotationhub", type=("build", "run"))
