# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRlmm(RPackage):
    """A Genotype Calling Algorithm for Affymetrix SNP Arrays

    A classification algorithm, based on a multi-chip, multi-SNP approach for Affymetrix SNP arrays. Using a large training sample where the genotype labels are known, this aglorithm will obtain more accurate classification results on new data. RLMM is based on a robust, linear model and uses the Mahalanobis distance for classification. The chip-to-chip non-biological variation is removed through normalization. This model-based algorithm captures the similarities across genotype groups and probes, as well as thousands other SNPs for accurate classification. NOTE: 100K-Xba only at for now.
    """

    homepage = "http://www.stat.berkeley.edu/users/nrabbee/RLMM"
    bioc = "RLMM"

    version("1.70.0", commit="d8ddab8c5f2e50b8112140f710448b9754d283cc")
    version("1.64.0", commit="03b58cede48a638d35c3a412af537a60eda0241d")

    depends_on("r@2.1:", type=("build", "run"))
    depends_on("r-mass", type=("build", "run"))
