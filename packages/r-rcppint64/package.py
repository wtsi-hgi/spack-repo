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
#     spack install r-rcppint64
#
# You can edit this file again by typing:
#
#     spack edit r-rcppint64
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class RRcppint64(RPackage):
    """'Int64' values can be created and accessed via the 'bit64' package and its 'integer64' class which package the 'int64' representation cleverly into a 'double'."""

    homepage = "https://github.com/eddelbuettel/rcppint64"
    cran = "RcppInt64"

    version("0.0.3", sha256="69bd4001de658e4edf8c1a297b7e9be5541778cd7e4b46c80b8929259fb62e37")
    version("0.0.2", sha256="c38be311d655728e8df96b741cbe68d6e8f1e5cb7fdee1fab8370414b166c849")
    version("0.0.1", sha256="3e0ffa9347fd8e295be5babc5bcfff1c59372c0b3afb6a791e11afcec1cedd11")

    depends_on("r-rcpp", type=("build", "run"))
    depends_on("r-tinytest", type=("build", "run"))
    depends_on("r-bit64", type=("build", "run"))
    depends_on("r-nanotime", type=("build", "run"))
