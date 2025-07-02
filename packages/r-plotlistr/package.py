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
#     spack install r-plotlistr
#
# You can edit this file again by typing:
#
#     spack edit r-plotlistr
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class RPlotlistr(RPackage):
    """Tools to work with lists of plots, allowing you to automatically generate plots 
    during an analysis and save them with sensible parameters."""

    homepage = "https://github.com/allydunham/plotlistr"
    git = "https://github.com/allydunham/plotlistr.git"

    license("LGPL-3.0")

    version("20200213", commit="8e421dcac73814e0223334d992fc12aba4605e18")

    depends_on("r@3.5.0:", type=("build", "run"))
    depends_on("r-ggplot2", type=("build", "run"))
    depends_on("r-multipanelfigure", type=("build", "run"))
