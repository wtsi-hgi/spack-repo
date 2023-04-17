# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLeidenbase(RPackage):
    """R and C/C++ Wrappers to Run the Leiden find_partition() Function.

    An R to C/C++ interface that runs the Leiden community
    detection algorithm to find a basic partition (). It runs the
    equivalent of the 'leidenalg' find_partition() function, which is
    given in the 'leidenalg' distribution file
    'leiden/src/functions.py'. This package includes the
    required source code files from the official 'leidenalg'
    distribution and functions from the R 'igraph'
    package.  The 'leidenalg' distribution is available from
    <https://github.com/vtraag/leidenalg/>
    and the R 'igraph' package is available from
    <https://igraph.org/r/>.
    The Leiden algorithm is described in the article by
    Traag et al. (2019) <doi:10.1038/s41598-019-41695-z>."""

    cran = "leidenbase"

    version("0.1.17", sha256="9adda0c6d7210f8c9ca8348e5c27ed18e6daef24305b57b032be78de65af4cb1")

    depends_on("r@3.5.0:", type=("build", "run"))
    depends_on("r-igraph", type=("build", "run"))
