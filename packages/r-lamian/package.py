# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
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
#     spack install r-lamian
#
# You can edit this file again by typing:
#
#     spack edit r-lamian
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class RLamian(RPackage):
    """Statistical Framework for Differential Pseudotime Analysis"""

    homepage = "https://github.com/Winnie09/Lamian"
    url = "https://github.com/Winnie09/Lamian/archive/refs/tags/v0.99.1.tar.gz"

    version("0.99.1", sha256="7b334ace44aa15789000ada5b95c7750e371781b05e1ea2bcda42722c39d7b55")

    depends_on("r@3.5.0:", type=("build", "run"))
    depends_on("r-complexheatmap", type=("build", "run"))
    depends_on("r-tscan", type=("build", "run"))
    depends_on("r-cairo", type=("build", "run"))
    depends_on("r-devtools", type=("build", "run"))
    depends_on("r-biocmanager", type=("build", "run"))
    depends_on("r-gridextra", type=("build", "run"))
    depends_on("r-matrixcalc", type=("build", "run"))
    depends_on("r-org-hs-eg-db", type=("build", "run"))
    depends_on("r-pheatmap", type=("build", "run"))
    depends_on("r-reshape2", type=("build", "run"))
    depends_on("r-scattermore", type=("build", "run"))
    depends_on("r-topgo", type=("build", "run"))
    depends_on("r-viridis", type=("build", "run"))
    depends_on("r-rhdf5", type=("build", "run"))
