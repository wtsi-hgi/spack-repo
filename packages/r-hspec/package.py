# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHspec(RPackage):
    """Hspec

    A package containing an environment representing the HGU133Plus2_Hs_Hspec.cdf file.
    """

    bioc = "Hspec"
    urls = [
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Hspec_0.99.1.tar.gz",
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/Hspec/Hspec_0.99.1.tar.gz",
    ]

    version(
        "0.99.1",
        sha256="ab9efed4e74db04fa104ff080ab55dcd962271e70240ff0f3bcf9c1468eceaa2",
    )

    depends_on("r@2.10:", type=("build", "run"))
    depends_on("r-annotationdbi", type=("build", "run"))
