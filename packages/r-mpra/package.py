# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMpra(RPackage):
    """Analyze massively parallel reporter assays

    Tools for data management, count preprocessing, and differential analysis in massively parallel report assays (MPRA).
    """

    homepage = "https://github.com/hansenlab/mpra"
    bioc = "mpra"

    version("1.30.1", commit="3ee57c997a2b0c4ce7f048bf4bd7480891dfae30")
    version("1.24.0", commit="3d39300ca09f693580f4ed60064cecc42ab927cf")

    depends_on("r@3.5:", type=("build", "run"))
    depends_on("r-biocgenerics", type=("build", "run"))
    depends_on("r-summarizedexperiment", type=("build", "run"))
    depends_on("r-limma", type=("build", "run"))
    depends_on("r-s4vectors", type=("build", "run"))
    depends_on("r-scales", type=("build", "run"))
    depends_on("r-statmod", type=("build", "run"))
