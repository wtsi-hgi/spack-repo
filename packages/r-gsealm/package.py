# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGsealm(RPackage):
    """Linear Model Toolset for Gene Set Enrichment Analysis

    Models and methods for fitting linear models to gene expression data, together with tools for computing and using various regression diagnostics.
    """

    bioc = "GSEAlm"

    version("1.68.0", commit="f593dce51fbb65ac3c00896f3230a9aa01e0ab37")
    version("1.62.0", commit="f035af140e6f4df5bfad6253972283fb181c7dba")

    depends_on("r-biobase", type=("build", "run"))
