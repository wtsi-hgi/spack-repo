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
#     spack install r-cowsay
#
# You can edit this file again by typing:
#
#     spack edit r-cowsay
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class RCowsay(RPackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://github.com/sckott/cowsay"
    cran = "cowsay"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers("github_user1", "github_user2")

    version("0.8.2", sha256="fd9766a336250e5eac05616c9d083b52abdd380244384ad7ba91273e26572db0")

    # FIXME: Add dependencies if required.
    depends_on("r-crayon", type=("build", "run"))
    depends_on("r-fortunes", type=("build", "run"))
    depends_on("r-rmsfact", type=("build", "run"))

