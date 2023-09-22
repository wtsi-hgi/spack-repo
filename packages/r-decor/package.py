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
#     spack install r-decor
#
# You can edit this file again by typing:
#
#     spack edit r-decor
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class RDecor(RPackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://github.com/r-lib/decor"
    cran = "decor"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers("github_user1", "github_user2")

    version("1.0.2", sha256="2e6c0cf3804253298c43c7cc64e389cf0ef2bebdca18753a487b9861e54671f6")

    # FIXME: Add dependencies if required.
    depends_on("r-tibble", type=("build", "run"))
    depends_on("r-vctrs", type=("build", "run"))

