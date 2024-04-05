# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class RLme4qtl(RPackage):
    """lme4qtl extends the lme4 R package for quantitative trait locus (qtl) mapping. It is all about the covariance structure of random effects. lme4qtl supports user-defined matrices for that, e.g. kinship or IBDs."""

    homepage = "https://github.com/variani/lme4qtl"
    url = "https://github.com/variani/lme4qtl/archive/refs/tags/0.1.10.tar.gz"

	version("0.1.10", sha256="59ae1e4aac83b55794cebdcda5529bdabab53a716213b964e6728468d8d594e8")

    depends_on("r-matrix", type=("build", "run"))
    depends_on("r-lme4", type=("build", "run"))
    depends_on("r-kinship2", type=("build", "run"))
    depends_on("r-plyr", type=("build", "run"))
    depends_on("r-tibble", type=("build", "run"))
    depends_on("r-ggplot2", type=("build", "run"))
