# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLowmacaannotation(RPackage):
    """LowMACAAnnotation

    A package containing the data to run LowMACA package.
    """

    bioc = "LowMACAAnnotation"
    urls = [
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/LowMACAAnnotation_0.99.3.tar.gz",
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/LowMACAAnnotation/LowMACAAnnotation_0.99.3.tar.gz",
    ]

    version(
        "0.99.3",
        sha256="959348611155b78a4b58452230a547af13028b674c06a826e748931259002366",
    )

    depends_on("r@2.10:", type=("build", "run"))
