# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAffyhgu133plus2expr(RPackage):
    """Affyhgu133Plus2Expr (GPL570) Expression Data Package

    Contains pre-built human (GPL570) database of gene expression profiles. The gene expression data was downloaded from NCBI GEO and preprocessed and normalized consistently. The biological context of each sample was recorded and manually verified based on the sample description in GEO.
    """

    bioc = "Affyhgu133Plus2Expr"

    version("1.42.0", commit="a1253951890403d19650701bc2153cedd47140ec")
    version("1.36.0", commit="4ab2e94a266df2eeea55918895a1f9381f0cf2fa")

    depends_on("r@2.10:", type=("build", "run"))
