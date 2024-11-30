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
#     spack install r-treemut
#
# You can edit this file again by typing:
#
#     spack edit r-treemut
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class RTreemut(RPackage):
    """Code implementing maximum likelihood assignment of mutations to trees. The method uses an EM method to soft assign mutations to branches and simultaneously estimate branch lengths."""

    homepage = "https://github.com/NickWilliamsSanger/treemut"
    git = "https://github.com/NickWilliamsSanger/treemut.git"

    version("20201113", commit="440ac2c42c773dcfe2ee51601d40e6ce85ab09df")

    depends_on("r-ape", type=("build", "run"))
