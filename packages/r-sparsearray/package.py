# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSparsearray(RPackage):
    """Efficient in-memory representation of multidimensional sparse arrays"""

    homepage = "https://bioconductor.org/packages/release/bioc/html/SparseArray.html"

    bioc = "SparseArray"
    urls = "https://bioconductor.org/packages/release/bioc/src/contrib/SparseArray_1.2.3.tar.gz"

    version("1.2.3", md5="86224ea83ca5df5984cfc6907c8f0bc1")

    depends_on("r@4.3.0:", type=("build", "run"))
    depends_on("r-matrix", type=("build", "run"))
    depends_on("r-matrixgenerics@1.11.1:", type=("build", "run"))
    depends_on("r-biocgenerics@0.43.1:", type=("build", "run"))
    depends_on("r-s4vectors", type=("build", "run"))
    depends_on("r-s4arrays@1.1.6:", type=("build", "run"))
    depends_on("r-matrixstats", type=("build", "run"))
    depends_on("r-iranges", type=("build", "run"))
    depends_on("r-xvector", type=("build", "run"))
