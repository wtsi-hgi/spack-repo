# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMergeomics(RPackage):
    """Integrative network analysis of omics data

    The Mergeomics pipeline serves as a flexible framework for integrating multidimensional omics-disease associations, functional genomics, canonical pathways and gene-gene interaction networks to generate mechanistic hypotheses. It includes two main parts, 1) Marker set enrichment analysis (MSEA); 2) Weighted Key Driver Analysis (wKDA).
    """

    bioc = "Mergeomics"

    version("1.36.0", commit="7ba9557405edaa91514ae7b586c3398fde278f1f")
    version("1.30.0", commit="e850a39f1a4218f0c45a9f4590e971726e48e89e")

    depends_on("r@3.0.1:", type=("build", "run"))
