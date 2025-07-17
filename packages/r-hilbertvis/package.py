# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHilbertvis(RPackage):
    """Hilbert curve visualization

    Functions to visualize long vectors of integer data by means of Hilbert curves
    """

    homepage = "http://www.ebi.ac.uk/~anders/hilbert"
    bioc = "HilbertVis"

    version("1.66.1", commit="b93932819cfb24ff9a67ff92fe7a351bba2fe808")
    version("1.60.0", commit="ad45689cf9643c9b0ac1b404a3f36e10d142e707")

    depends_on("r@2.6:", type=("build", "run"))
    depends_on("r-lattice", type=("build", "run"))
