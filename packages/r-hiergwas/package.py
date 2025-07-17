# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHiergwas(RPackage):
    """Asessing statistical significance in predictive GWA studies

    Testing individual SNPs, as well as arbitrarily large groups of SNPs in GWA studies, using a joint model of all SNPs. The method controls the FWER, and provides an automatic, data-driven refinement of the SNP clusters to smaller groups or single markers.
    """

    bioc = "hierGWAS"

    version("1.38.0", commit="0db2fedc656a4bfa2a70d4a15e9a2a7a93d209fb")
    version("1.32.0", commit="0217d7e88f2ee39d11d02fd1102af1ff5e3092d6")

    depends_on("r@3.2:", type=("build", "run"))
    depends_on("r-fastcluster", type=("build", "run"))
    depends_on("r-glmnet", type=("build", "run"))
    depends_on("r-fmsb", type=("build", "run"))
