# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMfuzz(RPackage):
    """Soft clustering of time series gene expression data

    Package for noise-robust soft clustering of gene expression time-series data (including a graphical user interface)
    """

    homepage = "http://mfuzz.sysbiolab.eu/"
    bioc = "Mfuzz"

    version("2.68.0", commit="a1937d8a94400453fc0ca3eacbe2b44ea54c679f")
    version("2.62.0", commit="b17f5af839c2a98feefaa31439f33702f340578a")

    depends_on("r@2.5:", type=("build", "run"))
    depends_on("r-biobase@2.5.5:", type=("build", "run"))
    depends_on("r-e1071", type=("build", "run"))
    depends_on("r-tkwidgets", type=("build", "run"))
