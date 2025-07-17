# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGeneattribution(RPackage):
    """Identification of candidate genes associated with genetic variation

    Identification of the most likely gene or genes through which variation at a given genomic locus in the human genome acts. The most basic functionality assumes that the closer gene is to the input locus, the more likely the gene is to be causative. Additionally, any empirical data that links genomic regions to genes (e.g. eQTL or genome conformation data) can be used if it is supplied in the UCSC .BED file format.
    """

    bioc = "geneAttribution"

    version("1.34.0", commit="4530c7dcba50961563cbdd88009e429ba0ebf5f6")
    version("1.28.0", commit="2d84296eac068ac39adf77d888ae62873932cede")

    depends_on("r-genomicranges", type=("build", "run"))
    depends_on("r-org-hs-eg-db", type=("build", "run"))
    depends_on("r-biocgenerics", type=("build", "run"))
    depends_on("r-genomeinfodb", type=("build", "run"))
    depends_on("r-genomicfeatures", type=("build", "run"))
    depends_on("r-iranges", type=("build", "run"))
    depends_on("r-rtracklayer", type=("build", "run"))
