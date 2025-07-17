# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMungesumstats(RPackage):
    """Standardise summary statistics from GWAS

    The *MungeSumstats* package is designed to facilitate the standardisation of GWAS summary statistics. It reformats inputted summary statisitics to include SNP, CHR, BP and can look up these values if any are missing. It also pefrorms dozens of QC and filtering steps to ensure high data quality and minimise inter-study differences.
    """

    homepage = "https://github.com/neurogenomics/MungeSumstats"
    bioc = "MungeSumstats"

    version("1.16.0", commit="e05f8e8ee1dc4d357d529daae7d20c7ed2c00201")
    version("1.10.1", commit="83ed5fbc5082f01ac19ad3a3d56e0b8061bd5ac9")

    depends_on("r@4.1:", type=("build", "run"))
    depends_on("r-magrittr", type=("build", "run"))
    depends_on("r-data-table", type=("build", "run"))
    depends_on("r-r-utils", type=("build", "run"))
    depends_on("r-dplyr", type=("build", "run"))
    depends_on("r-genomicranges", type=("build", "run"))
    depends_on("r-iranges", type=("build", "run"))
    depends_on("r-genomeinfodb", type=("build", "run"))
    depends_on("r-bsgenome", type=("build", "run"))
    depends_on("r-biostrings", type=("build", "run"))
    depends_on("r-stringr", type=("build", "run"))
    depends_on("r-variantannotation", type=("build", "run"))
    depends_on("r-googleauthr", type=("build", "run"))
    depends_on("r-httr", type=("build", "run"))
    depends_on("r-jsonlite", type=("build", "run"))
    depends_on("r-rtracklayer@1.59.1:", type=("build", "run"))
    depends_on("r-rcurl", type=("build", "run"))
