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
#     spack install r-gypsum
#
# You can edit this file again by typing:
#
#     spack edit r-gypsum
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class RGypsum(RPackage):
    """R/Bioconductor package 'gypsum'.

    Utility functions used by other Bioconductor packages to validate and
    manipulate metadata for resources published via ExperimentHub/AnnotationHub
    and related ecosystems.
    """

    homepage = "https://bioconductor.org/packages/gypsum"
    git = "https://git.bioconductor.org/packages/gypsum"
    bioc = "gypsum"

    # No release tarball discovery worked; pin to full Bioconductor commit.
    version("1.5.0", commit="205fc4202561a0c86cea404d3927204bc95ab29a")

    depends_on("r-httr2", type=("build", "run"))
    depends_on("r-jsonlite", type=("build", "run"))
    depends_on("r-filelock", type=("build", "run"))
    depends_on("r-rappdirs", type=("build", "run"))
