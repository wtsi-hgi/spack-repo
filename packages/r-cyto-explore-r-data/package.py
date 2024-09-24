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
#     spack install r-cyto-explore-r-data
#
# You can edit this file again by typing:
#
#     spack edit r-cyto-explore-r-data
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class RCytoExploreRData(RPackage):
    """Flow cytometry data for use in CytoExploreR."""

    homepage = "https://github.com/DillonHammill/CytoExploreRData"
    git = "https://github.com/DillonHammill/CytoExploreRData.git"

    version("20200827", commit="488edf083092247ad547172906efe6f8c2aa8700")
