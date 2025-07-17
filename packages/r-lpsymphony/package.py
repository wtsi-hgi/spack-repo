# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLpsymphony(RPackage):
    """Symphony integer linear programming solver in R

    This package was derived from Rsymphony_0.1-17 from CRAN. These packages provide an R interface to SYMPHONY, an open-source linear programming solver written in C++. The main difference between this package and Rsymphony is that it includes the solver source code (SYMPHONY version 5.6), while Rsymphony expects to find header and library files on the users' system. Thus the intention of lpsymphony is to provide an easy to install interface to SYMPHONY. For Windows, precompiled DLLs are included in this package.
    """

    homepage = "http://R-Forge.R-project.org/projects/rsymphony"
    bioc = "lpsymphony"

    version("1.36.0", commit="3811466d004118637d20e538cd2330e68d2a1090")
    version("1.30.0", commit="99258031e97ce12eb8d31bfb673b86a4786984a2")

    depends_on("r@3:", type=("build", "run"))
