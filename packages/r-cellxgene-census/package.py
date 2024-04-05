# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import inspect
from spack.package import *

class RCellxgeneCensus(RPackage):
    """The Census provides efficient computational tooling to access, query, and analyze all single-cell RNA data from CZ CELLxGENE Discover."""

    homepage = "https://chanzuckerberg.github.io/cellxgene-census"
    git = "https://github.com/chanzuckerberg/cellxgene-census"

    version("1.6.0", tag="v1.6.0")

    depends_on("r-aws-s3", type=("build", "run"))
    depends_on("r-dplyr", type=("build", "run"))
    depends_on("r-httr", type=("build", "run"))
    depends_on("r-jsonlite", type=("build", "run"))
    depends_on("r-tiledb-soma", type=("build", "run"))
    depends_on("r-tiledb", type=("build", "run"))
    depends_on("r-bit64", type=("build", "run"))
    depends_on("r-knitr", type=("build", "run"))
    depends_on("r-rmarkdown", type=("build", "run"))
    depends_on("r-singlecellexperiment@1.20.0:", type=("build", "run"))
    depends_on("r-seurat@4.1.0:", type=("build", "run"))
    depends_on("r-testthat@3.0.0:", type=("build", "run"))
    depends_on("r-withr", type=("build", "run"))
    #depends_on("cmake", type=("build"))

    def install(self, pkg, spec):
        args = ["--vanilla", "CMD", "INSTALL", "--library={0}".format(self.module.r_lib_dir), self.stage.source_path + "/api/r/cellxgene.census"]
        inspect.getmodule(self).R(*args)
