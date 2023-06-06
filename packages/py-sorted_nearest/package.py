# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PySortedNearest(PythonPackage):
    """Find nearest intervals."""

    git = "https://github.com/pyranges/sorted_nearest"

    version("0.0.39", sha256="e1b2a9e93abce34a868ee11e82931017b76b524d")
    
    depends_on("py-numpy", type=("build", "run"))
