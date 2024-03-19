# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *
import os

class PyBinarymap(PythonPackage):
    """Bbinary representation of protein or nucleotide sequences."""

    homepage = "https://jbloomlab.github.io/binarymap/"
    git = "https://github.com/jbloomlab/binarymap"
    pypi = "binarymap/binarymap-0.6.tar.gz"

    version("0.6", sha256="82d1794908633c864526f84c87720165af03606f454169954ec2e32c36bab317")

    depends_on("python@3.9.9", type=("build", "run"))
    depends_on("py-setuptools", type="build")

    depends_on("py-pandas@1.2:", type=("build", "run"))
    depends_on("py-scipy@1.1:", type=("build", "run"))
    depends_on("py-natsort@0.8:", type=("build", "run"))

