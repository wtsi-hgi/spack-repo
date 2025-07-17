# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMirna20cdf(RPackage):
    """mirna20cdf

    A package containing an environment representing the miRNA-2_0.cdf file.
    """

    bioc = "mirna20cdf"
    urls = [
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/mirna20cdf_2.18.0.tar.gz",
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/mirna20cdf/mirna20cdf_2.18.0.tar.gz",
    ]

    version(
        "2.18.0",
        sha256="d209e50f1f3846e27d553605ff866af7a97ec0966f807fa68a0ec915e589db17",
    )

    depends_on("r-annotationdbi", type=("build", "run"))
