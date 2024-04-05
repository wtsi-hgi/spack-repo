# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import inspect
from spack.package import *


class RTiledbSoma(RPackage):
    """This is the R implementation of the SOMA API specification."""

    homepage ="https://single-cell-data.github.io/TileDB-SOMA/"
    git = "https://github.com/single-cell-data/TileDB-SOMA"

	version("1.4.3", tag="1.4.3")

    depends_on("r-r6", type=("build", "run"))
    depends_on("r-matrix", type=("build", "run"))
    depends_on("r-bit64", type=("build", "run"))
    depends_on("r-tiledb@0.21.1:", type=("build", "run"))
    depends_on("r-arrow", type=("build", "run"))
    depends_on("r-fs", type=("build", "run"))
    depends_on("r-glue", type=("build", "run"))
    depends_on("r-urltools", type=("build", "run"))
    depends_on("r-rcpp", type=("build", "run"))
    depends_on("r-data-table", type=("build", "run"))
    depends_on("r-spdl", type=("build", "run"))
    depends_on("r-rlang", type=("build", "run"))
    depends_on("r-tibble", type=("build", "run"))
    depends_on("r-rmarkdown", type=("build", "run"))
    depends_on("r-knitr", type=("build", "run"))
    depends_on("r-withr", type=("build", "run"))
    depends_on("r-testthat", type=("build", "run"))
    depends_on("r-seuratobject@4.1.0:", type=("build", "run"))
    depends_on("r-singlecellexperiment@1.20.0:", type=("build", "run"))
    depends_on("r-summarizedexperiment@1.28.0:", type=("build", "run"))
    depends_on("r-s4vectors", type=("build", "run"))
    depends_on("cmake", type=("build"))

    def install(self, pkg, spec):
        args = ["--vanilla", "CMD", "INSTALL", "--library={0}".format(self.module.r_lib_dir), self.stage.source_path + "/apis/r/"]
        inspect.getmodule(self).R(*args)
