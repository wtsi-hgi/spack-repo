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
#     spack install r-figshare
#
# You can edit this file again by typing:
#
#     spack edit r-figshare
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class RFigshare(RPackage):
    """An R interface to 'figshare'."""

    homepage = "hhttps://github.com/ropensci-archive/rfigshare"
    cran = "rfigshare"

    version("0.3.8", sha256="b2a8b9d7e14bfca4ef499fa59f7d45cf17ffa5962ef1d2e8a94088e403e55083")

    depends_on("r-rjsonio", type=("build", "run"))
    depends_on("r-httr", type=("build", "run"))
    depends_on("r-httpuv", type=("build", "run"))
    depends_on("r-yaml", type=("build", "run"))
    depends_on("r-ggplot2", type=("build", "run"))
    depends_on("r-xml", type=("build", "run"))
