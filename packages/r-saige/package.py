# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack.package import *


class RSaige(RPackage):
    """SAIGE is an R package developed with Rcpp for genome-wide association tests in large-scale data sets and biobanks. The method

accounts for sample relatedness based on the generalized mixed models
allows for model fitting with either full or sparse genetic relationship matrix (GRM)
works for quantitative and binary traits
handles case-control imbalance of binary traits
computationally efficient for large data sets
performs single-variant association tests
provides effect size estimation through Firth’s Bias-Reduced Logistic Regression
performs conditional association analysis"""

    homepage = "https://saigegit.github.io/SAIGE-doc/"
    url = "https://github.com/saigegit/SAIGE/archive/refs/tags/v1.3.3.tar.gz"

    version("1.3.3", sha256="7d67ae1cd140dc883e3429d9538b6cb42feef04602f7c53e429e22c790e67440")
    version("1.0.9", sha256="eb5030877faf4a50d39ae28d6cd9b4aa8059cba42e1c91a4b20c32581a9f75f9")
    version("1.0.4", sha256="4b9dd64648b2c807aeda448c8b96091164ce019800efc8ebf5dc87979e590d08")
    version("1.0.3", sha256="79bcdc2abc68d8f112086a3d872102f5714bb0baaf59e876e9f08b1ad3a45e9f")
    version("1.0.2", sha256="57f4c89f78b0be5a8a00be1a507fb6cedd09fc747e683acb4a6295b6901034cb")
    version("1.0.1", sha256="7bf0bc07929eab047e042604283dc696d80e1a11e69faa8e6b0f16d85bcfaac9")
    version("1.0.0", sha256="e5870bb08ce96bf01d97fbee4887242e471f5622d0d58e7e8f0e8916d32b91fc")

    depends_on("r@3.6.1:", type=("build", "run"))
    depends_on("gcc@5.4:", type=("build", "run"))
    depends_on("cmake@3.14.1", type=("build", "run"))
    depends_on("cget", type=("build", "run"))
    depends_on("savvy", type=("build", "run"))
    depends_on("r-rcpp@1.0.7:", type=("build", "run"))
    depends_on("r-rcpparmadillo", type=("build", "run"))
    depends_on("r-rcppparallel", type=("build", "run"))
    depends_on("r-data-table", type=("build", "run"))
    depends_on("r-spatest@3.1.2", type=("build", "run"))
    depends_on("r-rcppeigen", type=("build", "run"))
    depends_on("r-matrix", type=("build", "run"))
    depends_on("r-bh", type=("build", "run"))
    depends_on("r-optparse", type=("build", "run"))
    depends_on("r-skat", type=("build", "run"))
    depends_on("r-qlcmatrix", type=("build", "run"))
    depends_on("r-rhpcblasctl", type=("build", "run"))
    depends_on("r-roxygen2", type=("build", "run"))
    depends_on("r-rversions", type=("build", "run"))
    depends_on("r-devtools", type=("build", "run"))
    depends_on("r-dplyr", type=("build", "run"))
    depends_on("r-dbplyr", type=("build", "run"))
    

