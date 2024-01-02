# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGrowthrates(RPackage):
    """A collection of methods to determine growth rates from experimental data, in particular from batch experiments and plate reader trials."""

    homepage = "https://cran.r-project.org/web/packages/growthrates/index.html"

    cran = "growthrates"
    version("0.8.4", sha256="3820afa6c1faffdef0439cf7f87f54c1e281f0e4c71a7a81942b4647bebe0813")

    depends_on("r+X", type=("build", "run"))
    depends_on("r-lattice", type=("build", "run"))
    depends_on("r-desolve", type=("build", "run"))
    
    depends_on("r-fme", type=("build", "run"))

