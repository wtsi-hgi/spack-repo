# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIslet(RPackage):
    """Individual-Specific ceLl typE referencing Tool

    ISLET is a method to conduct signal deconvolution for general -omics data. It can estimate the individual-specific and cell-type-specific reference panels, when there are multiple samples observed from each subject. It takes the input of the observed mixture data (feature by sample matrix), and the cell type mixture proportions (sample by cell type matrix), and the sample-to-subject information. It can solve for the reference panel on the individual-basis and conduct test to identify cell-type-specific differential expression (csDE) genes. It also improves estimated cell type mixture proportions by integrating personalized reference panels.
    """

    bioc = "ISLET"

    version("1.10.0", commit="5848b91e7a133cb5bc620ba5d350605700243a7a")
    version("1.4.0", commit="6df8c28607092a90d20cbeb538d6fc1c8fcfa801")

    depends_on("r@4.2:", type=("build", "run"))
    depends_on("r-matrix", type=("build", "run"))
    depends_on("r-biocparallel", type=("build", "run"))
    depends_on("r-summarizedexperiment", type=("build", "run"))
    depends_on("r-biocgenerics", type=("build", "run"))
    depends_on("r-lme4", type=("build", "run"))
    depends_on("r-nnls", type=("build", "run"))
    depends_on("r-purrr", type=("build", "run"))
    depends_on("r-abind", type=("build", "run"))
