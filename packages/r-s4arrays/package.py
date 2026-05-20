# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RS4arrays(RPackage):
    """Foundation of array-like containers in Bioconductor

    The S4Arrays package defines the Array virtual class to be extended by other S4 classes that wish to implement a container with an array-like semantic. It also provides: (1) low-level functionality meant to help the developer of such container to implement basic operations like display, subsetting, or coercion of their array-like objects to an ordinary matrix or array, and (2) a framework that facilitates block processing of array-like objects (typically on-disk objects).
    """

    homepage = "https://bioconductor.org/packages/S4Arrays"
    bioc = "S4Arrays"
    urls = [
        "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/S4Arrays_1.2.1.tar.gz",
        "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/S4Arrays/S4Arrays_1.2.1.tar.gz",
    ]
    git="https://git.bioconductor.org/packages/S4Arrays.git"

    version("1.8.0", tag="RELEASE_3_21")
    version("1.7.3", commit="41a64ffe40d2e1d2d7092631794de918b5fdab2c")
    version("1.6.0", tag="RELEASE_3_20")
    version("1.4.1", tag="RELEASE_3_19")
    version("1.2.1", tag="RELEASE_3_18")
    version("1.2.0", commit="bace32150ae231054cadc591a7f7e84f14d8faf0")
    version("1.1.1", commit="6074deee3b0edd47bfde20fa4151c54268e93d63")
    version("0.4.1", commit="09d02b41fbf2a514f176e740ee7ab7bbe2b60151")

    with default_args(type=("build", "run"))
    depends_on("r@4.3:", when="@0.5:")
    depends_on("r-matrix")
    depends_on("r-abind")
    depends_on("r-biocgenerics@0.45.2:")
    depends_on("r-s4vectors")
    depends_on("r-iranges")
    depends_on("r-crayon")
