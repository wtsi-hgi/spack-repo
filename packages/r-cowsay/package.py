# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class RCowsay(RPackage):
    """Messages, Warnings, Strings with Ascii Animals
    
    Allows printing of character strings as messages/warnings/etc. with ASCII animals, including cats, cows, frogs, chickens, ghosts, and more.
    """

    homepage = "https://github.com/sckott/cowsay"
    cran = "cowsay"

    version("0.8.2", sha256="fd9766a336250e5eac05616c9d083b52abdd380244384ad7ba91273e26572db0")

    depends_on("r-crayon", type=("build", "run"))
    depends_on("r-fortunes", type=("build", "run"))
    depends_on("r-rmsfact", type=("build", "run"))

