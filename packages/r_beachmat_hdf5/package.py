# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBeachmatHdf5(RPackage):
    """beachmat bindings for HDF5-backed matrices

    Extends beachmat to support initialization of tatami matrices from HDF5-backed arrays. This allows C++ code in downstream packages to directly call the HDF5 C/C++ library to access array data, without the need for block processing via DelayedArray. Some utilities are also provided for direct creation of an in-memory tatami matrix from a HDF5 file.
    """

    bioc = "beachmat.hdf5"
    urls = [
        "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/beachmat.hdf5_1.0.0.tar.gz",
        "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/beachmat.hdf5/beachmat.hdf5_1.0.0.tar.gz",
    ]

    version("1.6.0", tag="RELEASE_3_21")
    version(
        "1.0.0",
        md5="b2ca9b6358fb05895101e6a911ca0e39",
        url="https://www.bioconductor.org/packages/3.18/bioc/src/contrib/beachmat.hdf5_1.0.0.tar.gz",
    )

    depends_on("r-beachmat", type=("build", "run"))
    depends_on("r-assorthead", type=("build", "run"), when="@1.6:")
    depends_on("r-hdf5array", type=("build", "run"))
    depends_on("r-delayedarray", type=("build", "run"))
    depends_on("r-rcpp", type=("build", "run"))
    depends_on("r-rhdf5lib", type=("build", "run"))
    depends_on("zlib", type=("build", "link", "run"))
