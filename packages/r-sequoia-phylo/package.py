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
#     spack install r-sequoia-phylo
#
# You can edit this file again by typing:
#
#     spack edit r-sequoia-phylo
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class RSequoiaPhylo(BundlePackage):
    """Reconstructing phylogenetic trees from genome-wide somatic mutations in clonal samples."""

    homepage = "https://github.com/TimCoorens/Sequoia"
    git = "https://github.com/TimCoorens/Sequoia.git"

    license("GPL-3.0")

    version("20240305", commit="aa91ae217979dbf19dcaf490430c8e656b7692da")

    depends_on("r-ggplot2")
    depends_on("r-ape")
    depends_on("r-seqinr")
    depends_on("r-stringr")
    depends_on("r-data-table")
    depends_on("r-tidyr")
    depends_on("r-dplyr")
    depends_on("r-vgam")
    depends_on("r-mass")
    depends_on("r-devtools")
    depends_on("r-optparse")
    depends_on("r-rsamtools")
    depends_on("r-genomicranges")
    depends_on("r-treemut")
    depends_on("mpboot")
    depends_on("r-biocmanager")
