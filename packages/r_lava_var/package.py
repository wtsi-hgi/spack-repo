# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# ----------------------------------------------------------------------------
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install r-lava-var
#
# You can edit this file again by typing:
#
#     spack edit r-lava-var
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class RLavaVar(RPackage):
    """LAVA (Local Analysis of [co]Variant Association): A tool developed for local genetic correlation (rg) analysis."""

    homepage = "https://github.com/josefin-werme/LAVA"
    url = "https://github.com/josefin-werme/LAVA/archive/refs/tags/v0.1.0.tar.gz"

    version("0.1.0", sha256="5c13b224470b9ec4e56535eb638ec0e8f79bcfd7c79df6c226b400c8119c917b")
    version("0.0.7", sha256="dc66d7ab373315fb096327569c8fdd69dc9bc5211b10a5ac569b5d7835fa9ff5")

    depends_on("r-data-table", type=("build", "run"))
    depends_on("r-snpstats", type=("build", "run"))
    depends_on("r-matrixsampling", type=("build", "run"))
    depends_on("r-knitr", type=("build", "run"))
    depends_on("r-rmarkdown", type=("build", "run"))
