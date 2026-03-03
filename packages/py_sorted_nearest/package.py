# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PySortedNearest(PythonPackage):
    """Find nearest intervals.

    Cython helper library for pyranges. Find nearest interval in linear time at C speed.
    """

    homepage = "https://github.com/pyranges/sorted_nearest"
    pypi = "sorted_nearest/sorted_nearest-0.0.39.tar.gz"

    version("0.0.39", sha256="16a51d5db87ae226b47ace43c176bb672477a1b7ba8052ea9291a6356c9c69b1")

    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-setuptools", type="build")
    depends_on("py-cython")

