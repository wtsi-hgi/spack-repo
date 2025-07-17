# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDrugvsdisease(RPackage):
    """Comparison of disease and drug profiles using Gene set Enrichment Analysis

    This package generates ranked lists of differential gene expression for either disease or drug profiles. Input data can be downloaded from Array Express or GEO, or from local CEL files. Ranked lists of differential expression and associated p-values are calculated using Limma. Enrichment scores (Subramanian et al. PNAS 2005) are calculated to a reference set of default drug or disease profiles, or a set of custom data supplied by the user. Network visualisation of significant scores are output in Cytoscape format.
    """

    bioc = "DrugVsDisease"

    version("2.50.0", commit="94526b8e896e3e198f6d073cb1e25cc3a527ba73")
    version("2.44.0", commit="65afd5434824c50fba71efe20be18eba40324140")

    depends_on("r@2.10:", type=("build", "run"))
    depends_on("r-affy", type=("build", "run"))
    depends_on("r-limma", type=("build", "run"))
    depends_on("r-biomart", type=("build", "run"))
    depends_on("r-arrayexpress", type=("build", "run"))
    depends_on("r-geoquery", type=("build", "run"))
    depends_on("r-drugvsdiseasedata", type=("build", "run"))
    depends_on("r-cmap2data", type=("build", "run"))
    depends_on("r-qvalue", type=("build", "run"))
    depends_on("r-annotate", type=("build", "run"))
    depends_on("r-hgu133a-db", type=("build", "run"))
    depends_on("r-hgu133a2-db", type=("build", "run"))
    depends_on("r-hgu133plus2-db", type=("build", "run"))
    depends_on("r-runit", type=("build", "run"))
    depends_on("r-biocgenerics", type=("build", "run"))
    depends_on("r-xtable", type=("build", "run"))
