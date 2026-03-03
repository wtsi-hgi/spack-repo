# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
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
#     spack install r-frustratometer
#
# You can edit this file again by typing:
#
#     spack edit r-frustratometer
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class RFrustratometer(RPackage):
    """An R package for calculating energetic local frustration in protein structures.

    Additionally to the functionalities present at the web server, frustratometeR offers
    the possibility to analyse frustration across molecular dynamics simulations and to
    assess the effect of aminoacid variants."""

    homepage = "https://github.com/proteinphysiologylab/frustratometeR"
    url = "https://github.com/proteinphysiologylab/frustratometeR/archive/refs/tags/v1.0.tar.gz"

    license("GPL-3.0-only")

    version("1.0", sha256="975b0ae4c49471384759174eece6eb6da57e439ad6c75e507c77fbbce227e09e")

    # R package dependencies
    depends_on("r@3.6.3:", type=("build", "run"))
    depends_on("r-usethis", type=("build", "run"))
    depends_on("r-devtools", type=("build", "run"))
    depends_on("r-bio3d", type=("build", "run"))
    depends_on("r-ggplot2", type=("build", "run"))
    depends_on("r-ggrepel", type=("build", "run"))
    depends_on("r-reshape2", type=("build", "run"))
    depends_on("r-dplyr", type=("build", "run"))
    depends_on("r-igraph", type=("build", "run"))
    depends_on("r-factominer", type=("build", "run"))
    depends_on("r-hmisc", type=("build", "run"))
    depends_on("r-msa", type=("build", "run"))
    depends_on("r-magick", type=("build", "run"))
    depends_on("r-leiden", type=("build", "run"))

    # Python and Python package dependencies
    depends_on("python@3.7:3.9", type=("build", "run"))
    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-biopython", type=("build", "run"))
    depends_on("py-leidenalg", type=("build", "run"))

    # Other dependencies
    depends_on("wget", type=("run"))
    depends_on("py-pymol", type=("build", "run"))
    depends_on("imagemagick", type=("build", "run"))
    depends_on("perl", type=("build", "run"))
