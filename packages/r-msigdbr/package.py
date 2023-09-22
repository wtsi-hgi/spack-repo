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
#     spack install r-msigdbr
#
# You can edit this file again by typing:
#
#     spack edit r-msigdbr
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class RMsigdbr(RPackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://igordot.github.io/msigdbr/"
    cran = "msigdbr"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers("github_user1", "github_user2")

    version("7.5.1", sha256="dc30487bdf3594425ae9faec1ca0d7d0cd7278f4f177689133f92880e74acaca")

    # FIXME: Add dependencies if required.
    depends_on("r-babelgene", type=("build", "run"))
    depends_on("r-dplyr", type=("build", "run"))
    depends_on("r-magrittr", type=("build", "run"))
    depends_on("r-rlang", type=("build", "run"))
    depends_on("r-tibble", type=("build", "run"))
    depends_on("r-tidyselect", type=("build", "run"))
