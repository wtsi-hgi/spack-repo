# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSparsearray(RPackage):
    """Efficient in-memory representation of multidimensional sparse arrays

    The SparseArray package is an infrastructure package that provides an array-like container for efficient in-memory representation of multidimensional sparse data in R. The package defines the SparseArray virtual class and two concrete subclasses: COO_SparseArray and SVT_SparseArray. Each subclass uses its own internal representation of the nonzero multidimensional data, the "COO layout" and the "SVT layout", respectively. SVT_SparseArray objects mimic as much as possible the behavior of ordinary matrix and array objects in base R. In particular, they suppport most of the "standard matrix and array API" defined in base R and in the matrixStats package from CRAN.
    """

    homepage = "https://bioconductor.org/packages/SparseArray"
    bioc = "SparseArray"
    urls = [
        "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/SparseArray_1.2.4.tar.gz",
        "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/SparseArray/SparseArray_1.2.4.tar.gz",
    ]
    git = "https://git.bioconductor.org/packages/SparseArray.git"

    version("1.8.0", tag="RELEASE_3_21")
    version("1.2.4", tag="RELEASE_3_18")

    with default_args(type=("build", "run")):
        depends_on("r@4.3:")
        depends_on("r-matrix")
        depends_on("r-biocgenerics@0.43.1:")
        depends_on("r-matrixgenerics@1.11.1:")
        depends_on("r-s4vectors")
        depends_on("r-s4vectors@0.43.2:", when="@1.8.0:")
        depends_on("r-s4arrays@1.5.11:")
        depends_on("r-matrixstats")
        depends_on("r-iranges")
        depends_on("r-xvector")
