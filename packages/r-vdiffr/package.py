
# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVdiffr(RPackage):
    """Visual Regression Testing and Graphical Diffing
    
    An extension to the 'testthat' package that makes it easy to add graphical unit tests. It provides a Shiny application to manage the test cases.
    """

    homepage = "https://vdiffr.r-lib.org/"
    cran = "vdiffr"

    version("1.0.6", sha256="620194676791fbbb303ea998d12544017d97c4ee975fed1e416ae99de74d23d6")

    depends_on("r-diffobj", type=("build", "run"))
    depends_on("r-glue", type=("build", "run"))
    depends_on("r-htmltools", type=("build", "run"))
    depends_on("r-lifecycle", type=("build", "run"))
    depends_on("r-rlang", type=("build", "run"))
    depends_on("r-testthat", type=("build", "run"))
    depends_on("r-xml2", type=("build", "run"))
    depends_on("libpng", type=("build", "link"))
    depends_on("r-cpp11", type=("build", "run"))

