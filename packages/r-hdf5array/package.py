# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHdf5array(RPackage):
    """HDF5 backend for DelayedArray objects.

    Implements the HDF5Array and TENxMatrix classes, 2 convenient and
    memory-efficient array-like containers for on-disk representation of
    HDF5 datasets. HDF5Array is for datasets that use the conventional (i.e.
    dense) HDF5 representation. TENxMatrix is for datasets that use the
    HDF5-based sparse matrix representation from 10x Genomics (e.g. the 1.3
    Million Brain Cell Dataset). Both containers being DelayedArray
    extensions, they support all operations supported by DelayedArray
    objects. These operations can be either delayed or block-processed."""

    bioc = "HDF5Array"

    # version("1.36.0", commit="1e32d9f9fc78bddffd1600aee8e46d76fa296b71") # Requires R >= 4.5
    version("1.8.1", commit="3c9aa23d117bf489b6341708dc80c943bd1af11a")
    version("1.6.0", commit="95f2f8d3648143abe9dc77c76340c5edf4114c82")
    version("1.4.8", commit="79ab96d123c8da8f8ead81f678fe714c0958ff45")
    version("1.34.0", commit="dab3921857f932b050a79b6d81c7ea2f0063ac9f")
    version("1.30.1", commit="1aee703e5b54c1be0bca0d5643944ce34612e0d3")
    version("1.28.0", commit="8c839417c4a37c35330bd6f02b79dda9f48e76ae")
    version("1.26.0", commit="38b7bd603f7281245605048d8d57237e00b74d79")
    version("1.24.2", commit="fb213ba36631b04dfe754705f701f3a015c4fc82")
    version("1.24.1", commit="d002fe70c84baaadb62058ce467d6c1ea032d8f5")
    version("1.22.1", commit="b3f091fbc159609e8e0792d2bf9fbef52c6ceede")
    version("1.18.0", commit="d5bd55d170cb384fdebdf60751e1e28483782caa")
    version("1.12.3", commit="21c6077f3f789748a18f2e579110576c5522e975")
    version("1.10.1", commit="0b8ae1dfb56e4203dd8e14781850370df46a5e2c")

    depends_on("r@3.4:", type=("build", "run"))
    depends_on("r-delayedarray@0.31.8:", type=("build", "run"), when="@1.34:")
    depends_on("r-delayedarray@0.27.2:", type=("build", "run"), when="@1.30:")
    depends_on("r-delayedarray@0.26.1:", type=("build", "run"), when="@1.28:")
    depends_on("r-delayedarray@0.26.0", type=("build", "run"), when="@1.24")
    depends_on("r-delayedarray@0.15.6:", type=("build", "run"), when="@1.18:")
    depends_on("r-delayedarray@0.13.9:", type=("build", "run"), when="@1.16:")
    depends_on("r-delayedarray@0.12.3:", type=("build", "run"), when="@1.14:")
    depends_on("r-delayedarray@0.9.3:", type=("build", "run"), when="@1.12:")
    depends_on("r-delayedarray@0.7.41:", type=("build", "run"), when="@1.10:")
    depends_on("r-delayedarray@0.5.32:", type=("build", "run"), when="@1.8:")
    depends_on("r-delayedarray@0.3.18:", type=("build", "run"), when="@1.6:")
    depends_on("r-delayedarray@0.2.4:", type=("build", "run"), when="@1.4:")
    depends_on("r-rhdf5@2.31.6:", type=("build", "run"))
    depends_on("r-matrix", type=("build", "run"))
    depends_on("r-rhdf5filters", type=("build", "run"))
    depends_on("r-biocgenerics@0.31.5:", type=("build", "run"))
    depends_on("r-biocgenerics@0.51.2:", type=("build", "run"), when="@1.34:")
    depends_on("r-s4vectors@0.27.13:", type=("build", "run"))
    depends_on("r-iranges", type=("build", "run"))
    depends_on("r-s4arrays@1.1.1:", type=("build", "run"), when="@1.30:")
    depends_on("r-s4arrays@1.0.1:", type=("build", "run"), when="@1.26:")
    depends_on("r-rhdf5lib", type=("build", "run"))
    depends_on("zlib", type=("build", "link", "run"))
    # depends_on("r-h5mread", type=("build", "run"))  # Requires R >= 4.5
