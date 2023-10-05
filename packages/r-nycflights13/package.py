# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class RNycflights13(RPackage):
    """Airline on-time data for all flights departing NYC in 2013. Also includes useful 'metadata' on airlines, airports, weather, and planes."""

    homepage = "https://github.com/hadley/nycflights13"
    cran = "nycflights13"

    version("1.0.2", sha256="0e87c5a4e285f16750e91c75aeba33b1e4682cdabf4a3effe5a1de7398394a1d")
    version("1.0.1", sha256="acb6364219af854f68fbd513939ff8ae8cb99b530c045aa8dd9626797256dd5b")
    version("1.0.0", sha256="1626cae2329e23343fe797553c5a2af341cf7abe31d3545ca45bfb783b2b6081")
    version("0.2.2", sha256="cc13051face739eecf3a5a2654a53d51110b0aa3968cb47b5bfb95053dbfa7a0")
    version("0.2.1", sha256="d0eaca30d04bc39f67f8d364f451e046e9bcca2d68c2d9117d51f72e0b8eedaf")
    version("0.2.0", sha256="537d923e1f4a0806810d3d8861e6b86cfe090f69ef3e34a530f96e6bddabe498")
    version("0.1", sha256="0bb0a2dd9b5f5ed84d931d93316151d2ceb1e47ad8d8b948feed62dee1557895")

    depends_on("r-tibble", type=("build", "run"))
    depends_on("r-dplyr", type=("build", "run"))
