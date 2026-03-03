# Copyright 2013-2025 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RUdr(RPackage):
    """Ultimate Deconvolution for Multivariate Normal Means

    Implements algorithms for solving the multivariate normal means problem
    via empirical Bayes. The "Ultimate Deconvolution" name comes from its
    connection to the "Extreme Deconvolution" method.
    """

    homepage = "https://github.com/stephenslab/udr"
    url = "https://github.com/stephenslab/udr/archive/refs/tags/0.3.154.tar.gz"

    # Upstream tags use dots, DESCRIPTION shows 0.3-154; we follow tag versioning.
    version("0.3.154", sha256="35daedc9be9d8b1015962f24a530d2a3e8ae62a4f5947c8c3eae69b8ea1bfde2")

    # Core R dependency
    depends_on("r@3.5:", type=("build", "run"))

    # Imports
    depends_on("r-mvtnorm", type=("build", "run"))
    depends_on("r-rcpp@1.0.3:", type=("build", "run"))

    # LinkingTo
    depends_on("r-rcpparmadillo", type=("build", "run"))

