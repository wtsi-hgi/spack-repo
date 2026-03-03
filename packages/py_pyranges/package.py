# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyranges(PythonPackage):
    """GenomicRanges for Python."""

    homepage = "https://pyranges.github.io/pyranges"
    pypi = "pyranges/pyranges-0.0.127.tar.gz"

    version("0.0.127", sha256="92a59bf16b86e0aa35da9fdc30226038af9525417065bd07ba111f1efbd78aea")

    depends_on("py-pandas", type=("build", "run"))
    depends_on("py-ncls@0.0.63:", type=("build", "run"))
    depends_on("py-tabulate", type=("build", "run"))
    depends_on("py-sorted-nearest@0.0.33:", type=("build", "run"))
    depends_on("py-natsort", type=("build", "run"))
    depends_on("py-setuptools", type="build")
    depends_on("py-cython")


