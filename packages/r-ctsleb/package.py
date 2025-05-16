# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class RCtsleb(RPackage):
    """CT-SLEB is a method designed to generate multi-ancestry PRSs that incorporate existing large GWAS from EUR populations and smaller GWAS from non-EUR populations."""

    homepage = "https://github.com/andrewhaoyu/CTSLEB"
    url = "https://github.com/andrewhaoyu/CTSLEB/archive/refs/tags/v1.0.0.tar.gz"

    version("1.0.0", sha256="e4faf1a81e94e4d0fd5f2dde2250a19224b6842d214e5e7e3dd70ca51dda7549")

    depends_on("r-devtools", type=("build", "run"))
    depends_on("r-data-table", type=("build", "run"))
    depends_on("r-dplyr", type=("build", "run"))
    depends_on("r-caret", type=("build", "run"))
    depends_on("r-superlearner", type=("build", "run"))
    depends_on("r-ranger", type=("build", "run"))
    depends_on("r-glmnet", type=("build", "run"))
