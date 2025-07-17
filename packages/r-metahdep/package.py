# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMetahdep(RPackage):
    """Hierarchical Dependence in Meta-Analysis

    Tools for meta-analysis in the presence of hierarchical (and/or sampling) dependence, including with gene expression studies
    """

    bioc = "metahdep"

    version("1.66.0", commit="a03807f33ef8c44cc4d696f2d300b74e1a4bbca2")
    version("1.60.0", commit="187c10d6dec24236234c13fbb62f1452c0d28dbf")

    depends_on("r@2.10:", type=("build", "run"))
