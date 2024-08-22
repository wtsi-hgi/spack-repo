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
#     spack install r-deposits
#
# You can edit this file again by typing:
#
#     spack edit r-deposits
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class RDeposits(RPackage):
    """The deposits R package is a universal client for depositing and accessing research data in a variety of online deposition services. Currently supported services are zenodo and figshare. These two systems have fundamentally different interfaces (“API”s, or Application Programming Interfaces), and access to these and indeed all deposition services has traditionally been enabled through individual software clients. The deposits package aims to be a universal client offering access to a variety of deposition services, without users having to know any specific details of the APIs for each service."""

    homepage = "https://github.com/ropenscilabs/deposits"
    git = "https://github.com/ropenscilabs/deposits.git"

    license("MIT")

    version("20240219", commit="aaaf7f7ed3a3f6a587792032bf5ba245b5e3631b")

    depends_on("r-checkmate", type=("build", "run"))
    depends_on("r-fs", type=("build", "run"))
    depends_on("r-here", type=("build", "run"))
    depends_on("r-httr2", type=("build", "run"))
    depends_on("r-jsonlite", type=("build", "run"))
    depends_on("r-jsonvalidate", type=("build", "run"))
    depends_on("r-r6", type=("build", "run"))
    depends_on("r-withr", type=("build", "run"))
    depends_on("r-xml2", type=("build", "run"))
    depends_on("r-frictionless", type=("build", "run"))
    depends_on("r-knitr", type=("build", "run"))
    depends_on("r-pkgbuild", type=("build", "run"))
    depends_on("r-rmarkdown", type=("build", "run"))
    depends_on("r-testthat", type=("build", "run"))


