# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGp53cdf(RPackage):
    """gp53cdf

    A package containing an environment representing the GP53.CDF file.
    """

    bioc = "gp53cdf"
    urls = [
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/gp53cdf_2.18.0.tar.gz",
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/gp53cdf/gp53cdf_2.18.0.tar.gz",
    ]

    version(
        "2.18.0",
        sha256="7299772bb0eb4074106cb34c50f07ddd7f06ed26e3c9d1a3547821157b4ee686",
    )

    depends_on("r-annotationdbi", type=("build", "run"))
