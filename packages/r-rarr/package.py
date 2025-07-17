# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRarr(RPackage):
    """Read Zarr Files in R

    The Zarr specification defines a format for chunked, compressed, N-dimensional arrays.  It's design allows efficient access to subsets of the stored array, and supports both local and cloud storage systems. Rarr aims to implement this specifcation in R with minimal reliance on an external tools or libraries.
    """

    homepage = "https://github.com/grimbough/Rarr"
    bioc = "Rarr"

    version("1.8.0", commit="37eea8ddd387afacb81e62f8a763763ea8c78679")
    version("1.2.0", commit="e9d1a91253d3639d6429daebe86162255d76df07")

    depends_on("r-jsonlite", type=("build", "run"))
    depends_on("r-httr", type=("build", "run"))
    depends_on("r-stringr", type=("build", "run"))
    depends_on("r-r-utils", type=("build", "run"))
    depends_on("r-paws-storage", type=("build", "run"))
    depends_on("zlib", type=("build", "link", "run"))
