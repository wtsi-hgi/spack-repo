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
#     spack install r-illuminahumanmethylationepicv2anno-20a1-hg38
#
# You can edit this file again by typing:
#
#     spack edit r-illuminahumanmethylationepicv2anno-20a1-hg38
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class RIlluminahumanmethylationepicv2anno20a1Hg38(RPackage):
    """Annotation for Illumina HumanMethylation EPICv2 (20a1 hg38)."""

    homepage = "https://bioconductor.org/packages/IlluminaHumanMethylationEPICv2anno.20a1.hg38/"
    url = "https://www.bioconductor.org/packages/3.21/data/annotation/src/contrib/IlluminaHumanMethylationEPICv2anno.20a1.hg38_1.0.0.tar.gz"
    bioc = "IlluminaHumanMethylationEPICv2anno.20a1.hg38"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers("github_user1", "github_user2")

    # FIXME: Add the SPDX identifier of the project's license below.
    # See https://spdx.org/licenses/ for a list.
    license("Artistic-2.0")

    version("1.0.0", sha256="aae07c726c534fc017c5c730d2e3189120d2c73f52f5c4306a842a7cd4a8e46e")

    depends_on("r-minfi", type=("build", "run"))

    def install_args(self, spec, prefix):
        """Skip heavy docs for faster data package install."""
        return [
            "--no-build-vignettes",
            "--no-manual",
            "--no-test-load",
        ]
