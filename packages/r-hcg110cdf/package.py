# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHcg110cdf(RPackage):
    """hcg110cdf

    A package containing an environment representing the HC_G110.cdf file.
    """

    bioc = "hcg110cdf"
    urls = [
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/hcg110cdf_2.18.0.tar.gz",
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/hcg110cdf/hcg110cdf_2.18.0.tar.gz",
    ]

    version(
        "2.18.0",
        sha256="566d23bed8ca13fda93db22980a753fbd67477513009c5c9dfbab16475590888",
    )

    depends_on("r-annotationdbi", type=("build", "run"))
