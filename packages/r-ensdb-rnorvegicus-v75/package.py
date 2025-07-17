# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REnsdbRnorvegicusV75(RPackage):
    """Ensembl based annotation package

    Exposes an annotation databases generated from Ensembl.
    """

    bioc = "EnsDb.Rnorvegicus.v75"
    urls = [
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/EnsDb.Rnorvegicus.v75_2.99.0.tar.gz",
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/EnsDb.Rnorvegicus.v75/EnsDb.Rnorvegicus.v75_2.99.0.tar.gz",
    ]

    version(
        "2.99.0",
        md5="40ff53b41aa6fad0d5bd15f9c6f3bad8",
        url="https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/EnsDb.Rnorvegicus.v75_2.99.0.tar.gz",
    )

    depends_on("r-ensembldb", type=("build", "run"))
