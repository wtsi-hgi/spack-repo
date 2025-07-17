# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDresscheck(RPackage):
    """data and software for checking Dressman JCO 25(5) 2007

    data and software for checking Dressman JCO 25(5) 2007
    """

    bioc = "dressCheck"

    version("0.46.0", commit="36b4f9711cf0578886c150c7940623d8081d613c")
    version("0.40.0", commit="b1b3b5264d0dbd907e134e0e692f5ebbf84bf52b")

    depends_on("r@2.10.1:", type=("build", "run"))
    depends_on("r-biobase@2.5.5:", type=("build", "run"))
