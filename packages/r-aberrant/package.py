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
#     spack install r-aberrant
#
# You can edit this file again by typing:
#
#     spack edit r-aberrant
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class RAberrant(RPackage):
    """Aberrant R package from https://www.well.ox.ac.uk/~spencer/Aberrant/

    Aberrant is a super useful R package but it seems to no longer be available in CRAN. I am not the author of this software; rather, this is a mirror.

    When I use this package, I cite the following paper: Bellenguez, C. et al. A robust clustering algorithm for identifying problematic samples in genome-wide association studies. Bioinformatics 28, 134–135 (2012). PMID 22057162.
    """

    homepage = "https://github.com/carbocation/aberrant"
    git = "https://github.com/carbocation/aberrant"

    version("20200512", commit="1602293a79795953bb12c3c17ee53c5ec56f7f37")

    depends_on("r-mcmcpack", type=("build", "run"))
    depends_on("r-mvtnorm", type=("build", "run"))
    depends_on("r-ellipse", type=("build", "run"))

    def patch(self):
        with open("NAMESPACE", "w") as f:
            f.write('exportPattern( "." )')
