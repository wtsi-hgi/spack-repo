# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHilbertvisgui(RPackage):
    """HilbertVisGUI

    An interactive tool to visualize long vectors of integer data by means of Hilbert curves
    """

    homepage = "http://www.ebi.ac.uk/~anders/hilbert"
    bioc = "HilbertVisGUI"

    version("1.66.1", commit="5ca9b88b68cdd80e02a81dbabb6e52e611a632a5")
    version("1.60.0", commit="6e421a53a3bd38314648c0c766b8119b192918da")

    depends_on("r@2.6:", type=("build", "run"))
    depends_on("r-hilbertvis@1.1.6:", type=("build", "run"))
    depends_on("gtkmm@:2.24", type=("build", "link", "run"))
