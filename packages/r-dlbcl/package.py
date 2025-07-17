# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDlbcl(RPackage):
    """Diffuse large B-cell lymphoma expression data

    This package provides additional expression data on diffuse large B-cell lymphomas for the BioNet package.
    """

    homepage = "http://bionet.bioapps.biozentrum.uni-wuerzburg.de/"
    bioc = "DLBCL"

    version("1.48.0", commit="11233bcea5bfa1eae9a15ef77bdb515678d6ca12")
    version("1.42.2", commit="d6f5ff0b99910cc0b5fd6ba726cb099e8eac36c8")

    depends_on("r@2.11:", type=("build", "run"))
    depends_on("r-biobase", type=("build", "run"))
    depends_on("r-graph", type=("build", "run"))
