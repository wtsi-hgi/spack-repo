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
#     spack install r-xcell
#
# You can edit this file again by typing:
#
#     spack edit r-xcell
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class RXcell(RPackage):
    """xCell is a webtool that performs cell type enrichment analysis from gene expression data for 64 immune and stroma cell types."""

    homepage = "https://github.com/dviraran/xCell"
    url = "https://github.com/dviraran/xCell/archive/refs/tags/1.3.tar.gz"

    version("1.12", sha256="d204f4069708263b80920aa11e1a5815d9584c9e49237de7f40931856bec4cdf")
    version("1.11", sha256="b0c93714d26dd1d8453e19703b9073af9e6d9f179dfd1c46632ae0caee784142")
    version("1.3", sha256="9fc97603366f5ee318bc602beda60c6836bff7668bcb7a436bfc3af3cb919e44")
    version("1.2", sha256="52dcd5cfb5c8a4870cb485ee57f34d7830b23bdc61fd3012d859fdcc22ad941c")

    depends_on("r-gsva", type=("build", "run"))
    depends_on("r-gseabase", type=("build", "run"))
    depends_on("r-pracma", type=("build", "run"))
    depends_on("r-r-utils", type=("build", "run"))
    depends_on("r-mass", type=("build", "run"))
    depends_on("r-digest", type=("build", "run"))
    depends_on("r-curl", type=("build", "run"))
    depends_on("r-quadprog", type=("build", "run"))
    depends_on("r-knitr", type=("build", "run"))
    depends_on("r-rmarkdown", type=("build", "run"))
    depends_on("r-testthat", type=("build", "run"))
