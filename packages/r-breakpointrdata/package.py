# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBreakpointrdata(RPackage):
    """Strand-seq data for demonstration purposes

    Strand-seq data to demonstrate functionalities of breakpointR package.
    """

    homepage = "https://github.com/daewoooo/breakpointRdata"
    bioc = "breakpointRdata"

    version("1.26.0", commit="c5e399631086f47af4938445b8d00bcbb1846833")
    version("1.20.0", commit="5b19cbcb5f46629f45219f1808a83a7d7f73c5ab")

    depends_on("r@3.5:", type=("build", "run"))
