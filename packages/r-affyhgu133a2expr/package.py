# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAffyhgu133a2expr(RPackage):
    """Affymetrix Human Genome U133A 2.0 Array (GPL571) Expression Data Package

    Contains pre-built human (GPL571) databases of gene expression profiles. The gene expression data was downloaded from NCBI GEO and preprocessed and normalized consistently. The biological context of each sample was recorded and manually verified based on the sample description in GEO.
    """

    bioc = "Affyhgu133A2Expr"

    version("1.44.0", commit="7ffe34eb8ed65531ccce141c8dad068d3e2d12e5")
    version("1.38.0", commit="6015b5e62325349b1d42b0db7decdc8713eb30df")

    depends_on("r@2.10:", type=("build", "run"))
