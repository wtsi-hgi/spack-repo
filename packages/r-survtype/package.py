# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSurvtype(RPackage):
    """Subtype Identification with Survival Data

    Subtypes are defined as groups of samples that have distinct molecular and clinical features. Genomic data can be analyzed for discovering patient subtypes, associated with clinical data, especially for survival information. This package is aimed to identify subtypes that are both clinically relevant and biologically meaningful.
    """

    bioc = "survtype"

    version("1.24.0", commit="b2280c90820641111d05da23c4d7009d7998cfd2")
    version("1.18.0", commit="e5693695f628d13a9073e0fd85da7069f64ec28f")

    depends_on("r-summarizedexperiment", type=("build", "run"))
    depends_on("r-pheatmap", type=("build", "run"))
    depends_on("r-survival", type=("build", "run"))
    depends_on("r-survminer", type=("build", "run"))
    depends_on("r-clustvarsel", type=("build", "run"))
