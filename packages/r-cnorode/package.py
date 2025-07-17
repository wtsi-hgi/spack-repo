# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCnorode(RPackage):
    """ODE add-on to CellNOptR

    Logic based ordinary differential equation (ODE) add-on to CellNOptR.
    """

    bioc = "CNORode"

    version("1.50.0", commit="f85ceaf085ea80238d7a42a071e735a4674dc8b4")
    version("1.44.0", commit="ffe0ce3536d5acb68c73883a3fbb02730ad6f40c")

    depends_on("r-cellnoptr", type=("build", "run"))
    depends_on("r-genalg", type=("build", "run"))
    depends_on("r-knitr", type=("build", "run"))
