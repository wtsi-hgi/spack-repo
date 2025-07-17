# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCcimpute(RPackage):
    """ccImpute: an accurate and scalable consensus clustering based approach to impute dropout events in the single-cell RNA-seq data (https://doi.org/10.1186/s12859-022-04814-8)

    Dropout events make the lowly expressed genes indistinguishable from true zero expression and different than the low expression present in cells of the same type. This issue makes any subsequent downstream analysis difficult. ccImpute is an imputation algorithm that uses cell similarity established by consensus clustering to impute the most probable dropout events in the scRNA-seq datasets. ccImpute demonstrated performance which exceeds the performance of existing imputation approaches while introducing the least amount of new noise as measured by clustering performance characteristics on datasets with known cell identities.
    """

    bioc = "ccImpute"

    version("1.10.0", commit="9505c3c330a79f8ab5a7f73fea020c01eacc3a2c")
    version("1.4.0", commit="99d1fbcae7cc763527b51b6660cb7faf4a5b3cfa")

    depends_on("r-rcpp", type=("build", "run"))
    depends_on("r-matrixstats", type=("build", "run"))
    depends_on("r-simlr", type=("build", "run"))
    depends_on("r-biocparallel", type=("build", "run"))
    depends_on("r-rcppeigen", type=("build", "run"))
