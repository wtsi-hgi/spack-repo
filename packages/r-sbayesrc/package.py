# Copyright 2013-2023 Lawrence Livermore National Security, LLC
# and other Spack Project Developers. See the top-level COPYRIGHT
# file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSbayesrc(RPackage):
    """SBayesRC Method for Polygenic Prediction.

    Implements SBayesRC, which integrates functional annotations with
    high-density variants to improve polygenic prediction accuracy.
    """

    homepage = "https://github.com/zhilizheng/SBayesRC"
    url = "https://github.com/zhilizheng/SBayesRC/releases/download/v0.2.6/SBayesRC_0.2.6.tar.gz"
    license = "GPL-3+"

    version("0.2.6", sha256="dc556f1c3b295cfec37b0b2727fd4f043522c97bafe19be21acb049a57b78f49")

    depends_on("r@3.0.0:", type=("build", "run"))
    depends_on("r-data-table", type=("build", "run"))
    depends_on("r-rcpp", type=("build", "run"))
    depends_on("r-stringi", type=("build", "run"))
    depends_on("r-bh", type=("build", "run"))
    depends_on("r-rcppeigen", type=("build", "run"))
    depends_on("blas", type=("build", "link", "run"))

    def patch(self):
        """Ensure linking picks up a full BLAS implementation with ssyrk_."""
        blas_flags = self.spec["blas"].libs.ld_flags
        filter_file(
            "$(BLAS_LIBS)",
            f"$(BLAS_LIBS) {blas_flags}",
            "src/Makevars",
            string=True,
        )
