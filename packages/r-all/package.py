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
#     spack install r-all
#
# You can edit this file again by typing:
#
#     spack edit r-all
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class RAll(RPackage):
    """Data of T- and B-cell Acute Lymphocytic Leukemia from the Ritz Laboratory at the DFCI (includes Apr 2004 versions)."""

    url = "https://bioconductor.org/packages/release/data/experiment/src/contrib/ALL_1.42.0.tar.gz"
    bioc = "ALL"

    version("1.42.0", sha256="d1951905dea24bb4efe987ee2c22375b6de7ae6d5f4c47a2ec52ea23a6d65f7e")

    depends_on("r-biobase", type=("build", "run"))
