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
#     spack install r-illuminahumanmethylationepicv2manifest
#
# You can edit this file again by typing:
#
#     spack edit r-illuminahumanmethylationepicv2manifest
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class RIlluminahumanmethylationepicv2manifest(RPackage):
    """Manifest for Illumina's EPICv2 methylation arrays."""

    homepage = "https://bioconductor.org/packages/IlluminaHumanMethylationEPICv2manifest/"
    url = "https://www.bioconductor.org/packages/3.21/data/annotation/src/contrib/IlluminaHumanMethylationEPICv2manifest_1.0.0.tar.gz"
    bioc = "IlluminaHumanMethylationEPICv2manifest"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers("github_user1", "github_user2")

    # FIXME: Add the SPDX identifier of the project's license below.
    # See https://spdx.org/licenses/ for a list.
    license("Artistic-2.0")

    version("1.0.0", sha256="f41cbb23145daab677dbe49cc00a469b826e05a0900a0a313b222a867a098bfc")

    depends_on("r-minfi", type=("build", "run"))

    # No configure args for R data package
