# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMsmb(RPackage):
    """Data sets for the book 'Modern Statistics for Biology'

    Data sets for the book 'Modern Statistics for Modern Biology', S.P. Holmes and W. Huber.
    """

    bioc = "MSMB"

    version("1.26.0", commit="8c9291fdf4d2c2e7ebe126f7e9f705dad3ce4a8b")
    version("1.20.0", commit="2f9c7961cb30039c0c397fdaf4bc8915f11cbdf0")

    depends_on("r@3.5:", type=("build", "run"))
    depends_on("r-tibble", type=("build", "run"))
