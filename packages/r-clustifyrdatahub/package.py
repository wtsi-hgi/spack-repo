# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RClustifyrdatahub(RPackage):
    """External data sets for clustifyr in ExperimentHub

    References made from external single-cell mRNA sequencing data sets, stored as average gene expression matrices. For use with clustifyr <https://bioconductor.org/packages/clustifyr> to assign cell type identities.
    """

    homepage = "https://rnabioco.github.io/clustifyrdatahub/"
    bioc = "clustifyrdatahub"

    version("1.18.0", commit="cb13c46a1efbfc5d9aab984e4b695b64307b3a50")
    version("1.12.0", commit="f55a9d9a06e85eac5632052973e6175491975b21")

    depends_on("r@4:", type=("build", "run"))
    depends_on("r-experimenthub", type=("build", "run"))
