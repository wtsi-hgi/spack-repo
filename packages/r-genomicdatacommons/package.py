# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGenomicdatacommons(RPackage):
    """NIH / NCI Genomic Data Commons Access

    Programmatically access the NIH / NCI Genomic Data Commons RESTful service.
    """

    homepage = "https://bioconductor.org/packages/GenomicDataCommons"
    bioc = "GenomicDataCommons"

    version("1.32.1", commit="64b24d0a74bcd3e25d4cba194817d113829d7faf")
    version("1.26.0", commit="c8ad9dd930077ed749e1b8c5bb1ee57d2718b069")

    depends_on("r@3.4:", type=("build", "run"))
    depends_on("r-magrittr", type=("build", "run"))
    depends_on("r-httr", type=("build", "run"))
    depends_on("r-xml2", type=("build", "run"))
    depends_on("r-jsonlite", type=("build", "run"))
    depends_on("r-rlang", type=("build", "run"))
    depends_on("r-readr", type=("build", "run"))
    depends_on("r-genomicranges", type=("build", "run"))
    depends_on("r-iranges", type=("build", "run"))
    depends_on("r-dplyr", type=("build", "run"))
    depends_on("r-rappdirs", type=("build", "run"))
    depends_on("r-tibble", type=("build", "run"))
    depends_on("r-tidyr", type=("build", "run"))
