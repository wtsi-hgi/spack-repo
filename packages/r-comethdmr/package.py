# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RComethdmr(RPackage):
    """Accurate identification of co-methylated and differentially methylated regions in epigenome-wide association studies

    coMethDMR identifies genomic regions associated with continuous phenotypes by optimally leverages covariations among CpGs within predefined genomic regions. Instead of testing all CpGs within a genomic region, coMethDMR carries out an additional step that selects co-methylated sub-regions first without using any outcome information. Next, coMethDMR tests association between methylation within the sub-region and continuous phenotype using a random coefficient mixed effects model, which models both variations between CpG sites within the region and differential methylation simultaneously.
    """

    homepage = "https://github.com/TransBioInfoLab/coMethDMR"
    bioc = "coMethDMR"

    version("1.12.0", commit="0d1b6aed09b776481c9336feaa3ed50f4ae1aa2f")
    version("1.6.0", commit="aa833341f32a091d904d5018fb1f4dae96cf451e")

    depends_on("r@4.1:", type=("build", "run"))
    depends_on("r-annotationhub", type=("build", "run"))
    depends_on("r-biocparallel", type=("build", "run"))
    depends_on("r-bumphunter", type=("build", "run"))
    depends_on("r-experimenthub", type=("build", "run"))
    depends_on("r-genomicranges", type=("build", "run"))
    depends_on("r-iranges", type=("build", "run"))
    depends_on("r-lmertest", type=("build", "run"))
