# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCitruscdf(RPackage):
    """citruscdf

    A package containing an environment representing the Citrus.cdf file.
    """

    bioc = "citruscdf"
    urls = [
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/citruscdf_2.18.0.tar.gz",
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/citruscdf/citruscdf_2.18.0.tar.gz",
    ]

    version(
        "2.18.0",
        sha256="b61d847660cc87dc26dbd96c363a78d661223ae48658ef63d9640ed783ac468c",
    )

    depends_on("r-annotationdbi", type=("build", "run"))
