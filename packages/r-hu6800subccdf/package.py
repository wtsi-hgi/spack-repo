# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHu6800subccdf(RPackage):
    """hu6800subccdf

    A package containing an environment representing the Hu6800subC.CDF file.
    """

    bioc = "hu6800subccdf"
    urls = [
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/hu6800subccdf_2.18.0.tar.gz",
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/hu6800subccdf/hu6800subccdf_2.18.0.tar.gz",
    ]

    version(
        "2.18.0",
        sha256="b71435c42908b2efd96039376a07c21d9a6f0d313597775e1a0e432ecc1439f6",
    )

    depends_on("r-annotationdbi", type=("build", "run"))
