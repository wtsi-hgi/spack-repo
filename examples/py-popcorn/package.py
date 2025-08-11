# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyPopcorn(PythonPackage):
    """Popcorn is a program for estimating the correlation of causal variant effect sizes across populations in GWAS."""

    homepage = "https://github.com/brielin/Popcorn"
    git = "https://github.com/brielin/Popcorn.git"

    license("GPL-3.0")

    version("20250411", commit="82a307f19fb8188373fdd6838be92d457bf65e06")

    depends_on("py-setuptools", type="build")
    depends_on("py-numpy@1.14.2:")
    depends_on("py-scipy@1.0.1:")
    depends_on("py-pandas@0.22.0:")
    depends_on("py-pysnptools@0.3.9:")
    depends_on("py-bottleneck@1.0.0:")
    depends_on("py-statsmodels@0.8.0:")
    depends_on("py-matplotlib@1.5.1:")
    depends_on("r", type="run")  # Required for h2weight.R script

