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
    urls = [
        "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/HilbertVisGUI_1.60.0.tar.gz",
        "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/HilbertVisGUI/HilbertVisGUI_1.60.0.tar.gz",
    ]

    version("1.60.0", md5="e9e6a2cce82ff0dfcf0828ae7d123537")

    depends_on("r@2.6:", type=("build", "run"))
    depends_on("r-hilbertvis@1.1.6:", type=("build", "run"))
    depends_on("gtkmm@:2.24", type=("build", "link", "run"))
