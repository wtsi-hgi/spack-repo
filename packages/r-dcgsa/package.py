# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDcgsa(RPackage):
    """Distance-correlation based Gene Set Analysis for longitudinal gene expression profiles

    Distance-correlation based Gene Set Analysis for longitudinal gene expression profiles. In longitudinal studies, the gene expression profiles were collected at each visit from each subject and hence there are multiple measurements of the gene expression profiles for each subject. The dcGSA package could be used to assess the associations between gene sets and clinical outcomes of interest by fully taking advantage of the longitudinal nature of both the gene expression profiles and clinical outcomes.
    """

    bioc = "dcGSA"

    version("1.36.0", commit="57fca283ba738a4f5b6ee78e31e6470dd3b37bcf")
    version("1.30.0", commit="890b874a7ae1b71cf60a9ce70f5e7bba6e807596")

    depends_on("r@3.3:", type=("build", "run"))
    depends_on("r-matrix", type=("build", "run"))
    depends_on("r-biocparallel", type=("build", "run"))
