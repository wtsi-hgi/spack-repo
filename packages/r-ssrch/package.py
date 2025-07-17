# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSsrch(RPackage):
    """a simple search engine

    Demonstrate tokenization and a search gadget for collections of CSV files.
    """

    bioc = "ssrch"

    version("1.24.0", commit="afe43f7a2a4ed04dc19c8dd4bd9bc77e9037c92c")
    version("1.18.0", commit="98161e142282cdd943e66164f10ab9347ac19583")

    depends_on("r@3.6:", type=("build", "run"))
    depends_on("r-shiny", type=("build", "run"))
    depends_on("r-dt", type=("build", "run"))
